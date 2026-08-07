import pytest

from libcobblersignatures import cli


@pytest.fixture
def fresh_signatures(monkeypatch):
    new_signatures = cli.Signatures()
    monkeypatch.setattr(cli, "os_signatures", new_signatures)
    return new_signatures


def _make_breed_with_version(fresh_signatures, breed="suse", version="sles15"):
    fresh_signatures.addosbreed(breed)
    fresh_signatures.addosversion(0, version, None)
    return fresh_signatures.osbreeds[0].osversions[version]


def _prompt_for_field(field_choice):
    def _prompt(questions):
        name = questions[0]["name"]
        if name == "edit_information_os_version_which":
            return {"edit_information_os_version_which": "suse"}
        if name == "edit_information_os_version_which_2":
            return {"edit_information_os_version_which_2": "sles15"}
        if name == "edit_information_os_version":
            return {"edit_information_os_version": field_choice}
        raise AssertionError(f"Unexpected prompt: {name}")

    return _prompt


def test_import_menu_file_not_found_prints_friendly_message(monkeypatch, capsys):
    # Arrange
    main_menu_answers = iter(["Import", "Exit"])
    monkeypatch.setattr(cli.main_menu_questions, "ask", lambda: next(main_menu_answers))
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "File")
    monkeypatch.setattr(cli.import_menu_questions2, "ask", lambda: "/no/such/file.json")

    # Act
    with pytest.raises(SystemExit) as exc_info:
        cli.main()

    # Assert
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "Import failed" in captured.err


def test_export_menu_write_failure_prints_friendly_message(
    monkeypatch, capsys, tmp_path
):
    # Arrange
    main_menu_answers = iter(["Export", "Exit"])
    monkeypatch.setattr(cli.main_menu_questions, "ask", lambda: next(main_menu_answers))
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {
            "export_menu_target": "File",
            "export_menu_prettyprint_1": False,
            "export_menu_prettyprint_2": "",
        },
    )
    monkeypatch.setattr(cli.export_menu_questions2, "ask", lambda: str(tmp_path))

    # Act
    with pytest.raises(SystemExit) as exc_info:
        cli.main()

    # Assert
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "Export failed" in captured.err


# --- import_menu ---


def test_import_menu_file(monkeypatch, fresh_signatures, tmp_path):
    signatures_file = tmp_path / "signatures.json"
    signatures_file.write_text('{"breeds": {"suse": {}}}')
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "File")
    monkeypatch.setattr(cli.import_menu_questions2, "ask", lambda: str(signatures_file))

    cli.import_menu()

    assert [breed.name for breed in fresh_signatures.osbreeds] == ["suse"]


def test_import_menu_string(monkeypatch, fresh_signatures):
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "String")
    monkeypatch.setattr(
        cli.import_menu_questions2, "ask", lambda: '{"breeds": {"suse": {}}}'
    )

    cli.import_menu()

    assert [breed.name for breed in fresh_signatures.osbreeds] == ["suse"]


def test_import_menu_built_in(monkeypatch, fresh_signatures):
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "Built-In")

    cli.import_menu()

    assert len(fresh_signatures.osbreeds) > 0


def test_import_menu_go_back(monkeypatch, fresh_signatures, capsys):
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "Go back")

    cli.import_menu()

    assert fresh_signatures.osbreeds == []
    assert capsys.readouterr().out == ""


def test_import_menu_unknown_option(monkeypatch, fresh_signatures, capsys):
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "bogus")

    cli.import_menu()

    assert fresh_signatures.osbreeds == []
    assert "Unknown import option selected" in capsys.readouterr().out


def test_import_menu_empty_source(monkeypatch, fresh_signatures, capsys):
    monkeypatch.setattr(cli.import_menu_questions, "ask", lambda: "File")
    monkeypatch.setattr(cli.import_menu_questions2, "ask", lambda: "")

    cli.import_menu()

    assert fresh_signatures.osbreeds == []
    assert "Source was not entered correctly" in capsys.readouterr().out


# --- export_menu ---


def test_export_menu_string(monkeypatch, fresh_signatures, capsys):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {
            "export_menu_target": "String",
            "export_menu_prettyprint_1": False,
            "export_menu_prettyprint_2": "",
        },
    )

    cli.export_menu()

    assert capsys.readouterr().out.strip() == '{"breeds": {"suse": {}}}'


def test_export_menu_file(monkeypatch, fresh_signatures, tmp_path):
    fresh_signatures.addosbreed("suse")
    target = tmp_path / "out.json"
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {
            "export_menu_target": "File",
            "export_menu_prettyprint_1": False,
            "export_menu_prettyprint_2": "",
        },
    )
    monkeypatch.setattr(cli.export_menu_questions2, "ask", lambda: str(target))

    cli.export_menu()

    assert target.read_text() == '{"breeds": {"suse": {}}}'


def test_export_menu_go_back(monkeypatch):
    monkeypatch.setattr(
        cli.questionary, "prompt", lambda questions: {"export_menu_target": "Go back"}
    )

    cli.export_menu()  # should not raise


def test_export_menu_unknown_option(monkeypatch, capsys):
    monkeypatch.setattr(
        cli.questionary, "prompt", lambda questions: {"export_menu_target": "bogus"}
    )

    cli.export_menu()

    assert "Unknown option selected" in capsys.readouterr().out


def test_export_menu_file_empty_path(monkeypatch, fresh_signatures, capsys):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {
            "export_menu_target": "File",
            "export_menu_prettyprint_1": False,
            "export_menu_prettyprint_2": "",
        },
    )
    monkeypatch.setattr(cli.export_menu_questions2, "ask", lambda: "")

    cli.export_menu()

    assert (
        "Target path for the file was not entered correctly" in capsys.readouterr().out
    )


# --- edit_menu: Operating System Breeds ---


def test_edit_menu_add_breed(monkeypatch, fresh_signatures):
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Add Operating System Breed"
    )
    monkeypatch.setattr(cli.edit_add_os_breed, "ask", lambda: "suse")

    cli.edit_menu()

    assert [b.name for b in fresh_signatures.osbreeds] == ["suse"]


def test_edit_menu_add_breed_duplicate(monkeypatch, fresh_signatures, capsys):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Add Operating System Breed"
    )
    monkeypatch.setattr(cli.edit_add_os_breed, "ask", lambda: "suse")

    cli.edit_menu()

    assert len(fresh_signatures.osbreeds) == 1
    assert "already in the list" in capsys.readouterr().out


def test_edit_menu_add_breed_empty_name(monkeypatch, fresh_signatures, capsys):
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Add Operating System Breed"
    )
    monkeypatch.setattr(cli.edit_add_os_breed, "ask", lambda: "")

    cli.edit_menu()

    assert fresh_signatures.osbreeds == []
    assert "Empty Operating System Breed name is not allowed" in capsys.readouterr().out


def test_edit_menu_remove_breed(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Remove Operating System Breed"
    )
    monkeypatch.setattr(
        cli.questionary, "prompt", lambda questions: {"edit_remove_os_breed": "suse"}
    )

    cli.edit_menu()

    assert fresh_signatures.osbreeds == []


def test_edit_menu_remove_breed_not_found(monkeypatch, fresh_signatures, capsys):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Remove Operating System Breed"
    )
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {"edit_remove_os_breed": "missing"},
    )

    cli.edit_menu()

    assert len(fresh_signatures.osbreeds) == 1
    assert "not found" in capsys.readouterr().out


def test_edit_menu_rename_breed(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.edit_menu_questions,
        "ask",
        lambda: "Edit the name of an Operating System Breed",
    )
    monkeypatch.setattr(
        cli.questionary, "prompt", lambda questions: {"edit_name_os_breed_1": "suse"}
    )
    monkeypatch.setattr(cli.edit_name_os_breed_2, "ask", lambda: "opensuse")

    cli.edit_menu()

    assert fresh_signatures.osbreeds[0].name == "opensuse"


def test_edit_menu_rename_breed_not_found(monkeypatch, fresh_signatures, capsys):
    monkeypatch.setattr(
        cli.edit_menu_questions,
        "ask",
        lambda: "Edit the name of an Operating System Breed",
    )
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {"edit_name_os_breed_1": "missing"},
    )

    cli.edit_menu()

    assert "not found" in capsys.readouterr().out


# --- edit_menu: Operating System Versions ---


def test_edit_menu_add_os_version(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Add Operating System Version"
    )
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: (
            {"edit_add_os_version_1": "suse"}
            if questions[0]["name"] == "edit_add_os_version_1"
            else {"edit_add_os_version_2": "sles15"}
        ),
    )

    cli.edit_menu()

    assert "sles15" in fresh_signatures.osbreeds[0].osversions


def test_edit_menu_add_os_version_breed_not_found(
    monkeypatch, fresh_signatures, capsys
):
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Add Operating System Version"
    )
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {"edit_add_os_version_1": "missing"},
    )

    cli.edit_menu()

    assert "not found" in capsys.readouterr().out


def test_edit_menu_remove_os_version(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    fresh_signatures.addosversion(0, "sles15", None)
    monkeypatch.setattr(
        cli.edit_menu_questions, "ask", lambda: "Remove Operating System Version"
    )
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: (
            {"edit_remove_os_version_1": "suse"}
            if questions[0]["name"] == "edit_remove_os_version_1"
            else {"edit_remove_os_version_2": "sles15"}
        ),
    )

    cli.edit_menu()

    assert fresh_signatures.osbreeds[0].osversions == {}


# --- edit_menu: misc ---


def test_edit_menu_delegates_to_breed_version_info(monkeypatch):
    monkeypatch.setattr(
        cli.edit_menu_questions,
        "ask",
        lambda: "Edit the information of an Operating System Version",
    )
    called = []
    monkeypatch.setattr(
        cli, "edit_menu_breed_version_info", lambda: called.append(True)
    )

    cli.edit_menu()

    assert called == [True]


def test_edit_menu_start_from_scratch(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(cli.edit_menu_questions, "ask", lambda: "Start from scratch")

    cli.edit_menu()

    assert cli.os_signatures is not fresh_signatures
    assert cli.os_signatures.osbreeds == []


def test_edit_menu_go_back(monkeypatch, fresh_signatures):
    monkeypatch.setattr(cli.edit_menu_questions, "ask", lambda: "Go Back")

    cli.edit_menu()  # should not raise


def test_edit_menu_unknown_option(monkeypatch, capsys):
    monkeypatch.setattr(cli.edit_menu_questions, "ask", lambda: "bogus")

    cli.edit_menu()

    assert "Unknown option selected" in capsys.readouterr().out


# --- edit_menu_breed_version_info ---


@pytest.mark.parametrize(
    "field_choice,question_name,attribute",
    [
        ("version_file", "edit_menu_breed_version_version_file", "version_file"),
        (
            "version_file_regex",
            "edit_menu_breed_version_version_file_regex",
            "version_file_regex",
        ),
        ("kernel_arch", "edit_menu_breed_version_kernel_arch", "kernel_arch"),
        (
            "kernel_arch_regex",
            "edit_menu_breed_version_kernel_arch_regex",
            "kernel_arch_regex",
        ),
        ("kernel_file", "edit_menu_breed_version_kernel_file", "kernel_file"),
        ("initrd_file", "edit_menu_breed_version_initrd_file", "initrd_file"),
        (
            "default_autoinstall",
            "edit_menu_breed_version_default_autoinstall",
            "default_autoinstall",
        ),
        ("kernel_options", "edit_menu_breed_version_kernel_options", "kernel_options"),
        (
            "kernel_options_post",
            "edit_menu_breed_version_kernel_options_post",
            "kernel_options_post",
        ),
    ],
)
def test_edit_menu_breed_version_info_text_field(
    monkeypatch, fresh_signatures, field_choice, question_name, attribute
):
    version = _make_breed_with_version(fresh_signatures)
    monkeypatch.setattr(cli.questionary, "prompt", _prompt_for_field(field_choice))
    monkeypatch.setattr(getattr(cli, question_name), "ask", lambda: "new-value")

    cli.edit_menu_breed_version_info()

    assert getattr(version, attribute) == "new-value"


def test_edit_menu_breed_version_info_isolinux_ok(monkeypatch, fresh_signatures):
    version = _make_breed_with_version(fresh_signatures)
    monkeypatch.setattr(cli.questionary, "prompt", _prompt_for_field("isolinux_ok"))
    monkeypatch.setattr(cli.edit_menu_breed_version_isolinux_ok, "ask", lambda: True)

    cli.edit_menu_breed_version_info()

    assert version.isolinux_ok is True


@pytest.mark.parametrize(
    "field_choice,add_question_name,attribute",
    [
        ("signatures", "edit_menu_breed_version_signatures_add", "signatures"),
        (
            "supported_arches",
            "edit_menu_breed_version_supported_arches_add",
            "supported_arches",
        ),
        (
            "supported_repo_breeds",
            "edit_menu_breed_version_supported_repo_breeds_add",
            "supported_repo_breeds",
        ),
        ("boot_files", "edit_menu_breed_version_boot_files_add", "boot_files"),
    ],
)
def test_edit_menu_breed_version_info_collection_field_add(
    monkeypatch, fresh_signatures, field_choice, add_question_name, attribute
):
    version = _make_breed_with_version(fresh_signatures)
    monkeypatch.setattr(cli.questionary, "prompt", _prompt_for_field(field_choice))
    monkeypatch.setattr(cli.edit_menu_version_add_remove_edit, "ask", lambda: "Add")
    monkeypatch.setattr(getattr(cli, add_question_name), "ask", lambda: "new-entry")

    cli.edit_menu_breed_version_info()

    assert "new-entry" in getattr(version, attribute)


def test_edit_menu_breed_version_info_go_back(monkeypatch, fresh_signatures):
    fresh_signatures.addosbreed("suse")
    monkeypatch.setattr(
        cli.questionary,
        "prompt",
        lambda questions: {"edit_information_os_version_which": "Go Back"},
    )

    cli.edit_menu_breed_version_info()  # should not raise


# --- helper functions ---


def test_get_os_breed_names(fresh_signatures):
    fresh_signatures.addosbreed("suse")
    fresh_signatures.addosbreed("redhat")

    assert cli.get_os_breed_names() == ["suse", "redhat"]


def test_get_os_version_names(fresh_signatures):
    fresh_signatures.addosbreed("suse")
    fresh_signatures.addosversion(0, "sles15", None)

    assert cli.get_os_version_names("suse") == ["sles15"]


def test_get_os_version_names_breed_not_found(fresh_signatures, capsys):
    assert cli.get_os_version_names("missing") == []
    assert "not found" in capsys.readouterr().out


def test_update_choices_appends_go_back():
    question = [{"choices": []}]

    cli.update_choices(question, ["a", "b"])

    assert question[0]["choices"] == ["a", "b", "Go Back"]
