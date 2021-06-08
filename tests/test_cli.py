"""
Unit tests for the CLI
See https://github.com/tmbo/questionary/tree/master/tests for examples and how to use
"""

import pytest
from tests.utils import KI, feed_cli_with_input


def test_abort_with_ctr_c():
    message = "Abort with CTRL + C"
    kwargs = {"choices": ["Yes", "No"]}
    text = KI.CONTROLC

    with pytest.raises(KeyboardInterrupt):
        feed_cli_with_input("select", message, text, **kwargs)


@pytest.mark.parametrize("expected_result,key_input", [
    ("Import", KI.ENT + "\r"),
    ("Export", KI.D + KI.ENT + "\r"),
    ("Edit", KI.D + KI.D + KI.ENT + "\r"),
    ("Exit", KI.D + KI.D + KI.D + KI.ENT + "\r")
])
def test_main_menu_questions(expected_result, key_input):
    # Arrange
    message = "What do you want to do?"
    kwargs = {"choices": ["Import", "Export", "Edit", "Exit"]}

    # Act
    result, cli = feed_cli_with_input("select", message, key_input, **kwargs)
    print(result)

    # Assert
    assert result == expected_result


@pytest.mark.parametrize("expected_result,key_input", [
    ("URL", KI.ENT + "\r"),
    ("String", KI.D + KI.ENT + "\r"),
    ("File", KI.D + KI.D + KI.ENT + "\r"),
    ("Go back", KI.D + KI.D + KI.D + KI.ENT + "\r")
])
def test_import_menu_questions(expected_result, key_input):
    # Arrange
    message = "What is your desired source of input?"
    kwargs = {"choices": ["URL", "String", "File", "Go back"]}

    # Act
    result, cli = feed_cli_with_input("select", message, key_input, **kwargs)
    print(result)

    # Assert
    assert result == expected_result


@pytest.mark.parametrize("expected_result,key_input", [
    # FIXME: Has to be only one slash (/) for unknown reason
    ("https:/raw.githubusercontent.com/cobbler/cobbler/master/config/cobbler/distro_signatures.json",
     "https://raw.githubusercontent.com/cobbler/cobbler/master/config/cobbler/distro_signatures.json"
     + KI.ENT),
    ("Test", "Test" + KI.D + KI.ENT),
    ("tests/test_data/distro_signatures.json", "tests/test_data/distro_signatures.json" + KI.D + KI.D + KI.ENT)
])
def test_import_menu_questions2(expected_result, key_input):
    # Arrange
    message = "Please enter the json in a single line or the source in a single line:"

    # Act
    result, cli = feed_cli_with_input("path", message, key_input)

    # Assert
    assert result == expected_result


@pytest.mark.parametrize("expected_result,key_input", [
    ("String", KI.ENT + "\r"),
    ("File", KI.D + KI.ENT + "\r"),
    ("Go back", KI.D + KI.D + KI.ENT + "\r")
])
def test_export_menu_questions(expected_result, key_input):
    # Arrange
    message = "What is your desired export target?"
    kwargs = {"choices": ["String", "File", "Go back"]}

    # Act
    result, cli = feed_cli_with_input("select", message, key_input, **kwargs)
    print(result)

    # Assert
    assert result == expected_result


def test_export_menu_questions2():
    # Arrange
    message = "Please enter the target path"
    text = "test.json\r"

    # Act
    result, cli = feed_cli_with_input("text", message, text)

    # Assert
    assert result == "test.json"


@pytest.mark.parametrize("expected_result,key_input", [
    ("Add Operating System Breed", KI.ENT + "\r"),
    ("Remove Operating System Breed", KI.D + KI.ENT + "\r"),
    ("Edit the name of an Operating System Breed", KI.D + KI.D + KI.ENT + "\r"),
    ("Add Operating System Version", KI.D + KI.D + KI.D + KI.ENT + "\r"),
    ("Remove Operating System Version", KI.D + KI.D + KI.D + KI.D + KI.ENT + "\r"),
    ("Edit the information of an Operating System Version", KI.D + KI.D + KI.D + KI.D + KI.D + KI.ENT + "\r"),
    ("Start from scratch", KI.D + KI.D + KI.D + KI.D + KI.D + KI.D + KI.ENT + "\r"),
    ("Go back", KI.D + KI.D + KI.D + KI.D + KI.D + KI.D + KI.D + KI.ENT + "\r"),
])
def test_edit_menu_questions(expected_result, key_input):
    # Arrange
    message = "What do you want to do?"
    kwargs = {"choices": ["Add Operating System Breed",
                          "Remove Operating System Breed",
                          "Edit the name of an Operating System Breed",
                          "Add Operating System Version",
                          "Remove Operating System Version",
                          "Edit the information of an Operating System Version",
                          "Start from scratch",
                          "Go back"]}

    # Act
    result, cli = feed_cli_with_input("select", message, key_input, **kwargs)
    print(result)

    # Assert
    assert result == expected_result
