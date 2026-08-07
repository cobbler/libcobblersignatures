"""
Keeps the ``description`` fields in ``libcobblersignatures/data/v2/schema.json`` and the key
reference table in ``docs/json-specification.rst`` in sync with the :class:`Osversion` model.

The first line of each property's docstring in :class:`Osversion` is the single source of truth.
Run this script whenever a docstring changes:

    python -m scripts.sync_json_spec_docs          # regenerate the files
    python -m scripts.sync_json_spec_docs --check  # verify only, exit 1 on drift
"""

import argparse
import difflib
import inspect
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

from libcobblersignatures.models.osversion import Osversion

REPO_ROOT = Path(__file__).resolve().parent.parent
V2_SCHEMA_PATH = REPO_ROOT / "libcobblersignatures" / "data" / "v2" / "schema.json"
JSON_SPEC_RST_PATH = REPO_ROOT / "docs" / "json-specification.rst"

TABLE_START = ".. sync-json-spec-docs: start"
TABLE_END = ".. sync-json-spec-docs: end"

_INLINE_CODE_RE = re.compile(r"``(.+?)``")


def _first_paragraph(docstring: str) -> str:
    """
    Joins the docstring's leading lines up to the first blank line into a single string, so the
    source can hard-wrap the summary across multiple lines (e.g. to respect a line-length limit)
    without truncating it.
    """
    paragraph_lines = []
    for line in inspect.cleandoc(docstring).splitlines():
        if not line.strip():
            break
        paragraph_lines.append(line.strip())
    return " ".join(paragraph_lines)


def get_property_docs() -> "OrderedDict[str, str]":
    """
    Returns the first docstring paragraph of every property defined on :class:`Osversion`, keyed
    by property name.
    """
    docs: "OrderedDict[str, str]" = OrderedDict()
    for name, member in inspect.getmembers(
        Osversion, lambda o: isinstance(o, property)
    ):
        if member.fget is None or not member.fget.__doc__:
            continue
        docs[name] = _first_paragraph(member.fget.__doc__)
    return docs


def to_plain_text(line: str) -> str:
    """
    Strips RST inline literal markup (````like this````) since the JSON schema has no RST
    renderer.
    """
    return _INLINE_CODE_RE.sub(r"\1", line)


def sync_schema_text(raw_text: str, property_docs: "OrderedDict[str, str]") -> str:
    """
    Replaces the ``"description"`` value of every property object whose key matches an
    :class:`Osversion` property name, leaving everything else in the file byte-for-byte
    untouched (indentation, key order, unrelated fields).
    """
    text = raw_text
    for key, doc in property_docs.items():
        pattern = re.compile(
            r'("'
            + re.escape(key)
            + r'"\s*:\s*\{.*?"description"\s*:\s*)"(?:[^"\\]|\\.)*"',
            re.DOTALL,
        )
        replacement = json.dumps(to_plain_text(doc))
        text, count = pattern.subn(lambda m: m.group(1) + replacement, text, count=1)
    return text


def _find_version_properties(node) -> list:
    """
    Recursively finds the ``properties`` object describing a single OS version, identified by
    containing both a ``signatures`` and a ``kernel_arch`` sibling key.
    """
    matches = []
    if isinstance(node, dict):
        if "signatures" in node and "kernel_arch" in node:
            matches.append(node)
        for value in node.values():
            matches.extend(_find_version_properties(value))
    elif isinstance(node, list):
        for item in node:
            matches.extend(_find_version_properties(item))
    return matches


def _load_version_properties() -> "OrderedDict[str, dict]":
    with open(V2_SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f, object_pairs_hook=OrderedDict)
    matches = _find_version_properties(schema)
    if not matches:
        raise RuntimeError(
            f"Could not locate the OS-version 'properties' object in {V2_SCHEMA_PATH}"
        )
    return matches[0]


def _type_label(prop_schema: dict) -> str:
    type_ = prop_schema.get("type", "")
    if isinstance(type_, list):
        return " / ".join(type_)
    return type_ or ""


def build_table_rst(property_docs: "OrderedDict[str, str]") -> str:
    """
    Builds the RST ``list-table`` block. Row order and the Type column come from the schema
    (the actual JSON structure); the Description column comes from the model docstrings.
    """
    version_properties = _load_version_properties()

    lines = [
        TABLE_START,
        "",
        ".. list-table:: ``signatures.json`` version keys",
        "   :header-rows: 1",
        "",
        "   * - Key",
        "     - Type",
        "     - Description",
    ]
    for key, prop_schema in version_properties.items():
        if key not in property_docs:
            continue
        lines.append(f"   * - ``{key}``")
        lines.append(f"     - {_type_label(prop_schema)}")
        lines.append(f"     - {property_docs[key]}")
    lines.append("")
    lines.append(TABLE_END)
    return "\n".join(lines) + "\n"


def sync_rst_text(raw_text: str, table: str) -> str:
    pattern = re.compile(
        re.escape(TABLE_START) + r".*?" + re.escape(TABLE_END) + r"\n?",
        re.DOTALL,
    )
    if not pattern.search(raw_text):
        raise RuntimeError(
            f"Could not find '{TABLE_START}' / '{TABLE_END}' markers in {JSON_SPEC_RST_PATH}"
        )
    return pattern.sub(lambda _m: table, raw_text)


def _diff(path: Path, old: str, new: str) -> str:
    return "".join(
        difflib.unified_diff(
            old.splitlines(keepends=True),
            new.splitlines(keepends=True),
            fromfile=f"{path} (on disk)",
            tofile=f"{path} (generated)",
        )
    )


def check() -> str:
    """
    Regenerates both files in memory and returns a unified diff against what's on disk. An empty
    string means everything is already in sync.
    """
    property_docs = get_property_docs()

    old_schema = V2_SCHEMA_PATH.read_text(encoding="utf-8")
    new_schema = sync_schema_text(old_schema, property_docs)

    old_rst = JSON_SPEC_RST_PATH.read_text(encoding="utf-8")
    new_rst = sync_rst_text(old_rst, build_table_rst(property_docs))

    return _diff(V2_SCHEMA_PATH, old_schema, new_schema) + _diff(
        JSON_SPEC_RST_PATH, old_rst, new_rst
    )


def write() -> None:
    property_docs = get_property_docs()

    old_schema = V2_SCHEMA_PATH.read_text(encoding="utf-8")
    new_schema = sync_schema_text(old_schema, property_docs)
    if new_schema != old_schema:
        V2_SCHEMA_PATH.write_text(new_schema, encoding="utf-8")

    old_rst = JSON_SPEC_RST_PATH.read_text(encoding="utf-8")
    new_rst = sync_rst_text(old_rst, build_table_rst(property_docs))
    if new_rst != old_rst:
        JSON_SPEC_RST_PATH.write_text(new_rst, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify without writing; print a diff and exit 1 on drift.",
    )
    args = parser.parse_args()

    if args.check:
        diff = check()
        if diff:
            print(diff, file=sys.stderr)
            sys.exit(1)
        sys.exit(0)

    write()


if __name__ == "__main__":
    main()
