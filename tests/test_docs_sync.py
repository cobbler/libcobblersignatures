from scripts.sync_json_spec_docs import check


def test_json_spec_docs_are_in_sync():
    diff = check()
    assert not diff, (
        "libcobblersignatures/data/v2/schema.json and/or docs/json-specification.rst are out of "
        "sync with the Osversion docstrings. Run `python -m scripts.sync_json_spec_docs` and "
        "commit the result:\n\n" + diff
    )
