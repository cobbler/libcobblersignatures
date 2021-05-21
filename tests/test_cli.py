"""
Unit tests for the CLI
"""

import pytest
from tests.utils import KeyInputs, feed_cli_with_input


def test_abort_with_ctr_c():
    message = "Abort with CTRL + C"
    kwargs = {"choices": ["Yes", "No"]}
    text = KeyInputs.CONTROLC

    with pytest.raises(KeyboardInterrupt):
        feed_cli_with_input("select", message, text, **kwargs)


@pytest.mark.parametrize("expected_result,key_input", [
    ("Import", KeyInputs.ENTER + "\r"),
    ("Export", KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Edit", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Exit", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r")
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
    ("URL", KeyInputs.ENTER + "\r"),
    ("String", KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("File", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Go back", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r")
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
     + KeyInputs.ENTER),
    ("Test", "Test" + KeyInputs.DOWN + KeyInputs.ENTER),
    ("tests/test_data/distro_signatures.json", "tests/test_data/distro_signatures.json" + KeyInputs.DOWN
     + KeyInputs.DOWN + KeyInputs.ENTER)
])
def test_import_menu_questions2(expected_result, key_input):
    # Arrange
    message = "Please enter the json in a single line or the source in a single line:"

    # Act
    result, cli = feed_cli_with_input("path", message, key_input)

    # Assert
    assert result == expected_result


@pytest.mark.parametrize("expected_result,key_input", [
    ("String", KeyInputs.ENTER + "\r"),
    ("File", KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Go back", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r")
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

    # Aact
    result, cli = feed_cli_with_input("text", message, text)

    # Assert
    assert result == "test.json"


@pytest.mark.parametrize("expected_result,key_input", [
    ("Add Operating System Breed", KeyInputs.ENTER + "\r"),
    ("Remove Operating System Breed", KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Edit the name of an Operating System Breed", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Add Operating System Version", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Remove Operating System Version", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN
     + KeyInputs.ENTER + "\r"),
    ("Edit the information of an Operating System Version", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN
     + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Start from scratch", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN
     + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
    ("Go back", KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN + KeyInputs.DOWN
     + KeyInputs.DOWN + KeyInputs.ENTER + "\r"),
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
