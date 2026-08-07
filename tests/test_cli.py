import pytest

from libcobblersignatures import cli


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
