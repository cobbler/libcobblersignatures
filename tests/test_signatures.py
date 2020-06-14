import pytest

from libcobblersignatures.signatures import Signatures, ImportTypes


def test_breeds():
    # Arrange
    signatures = Signatures()

    # Act
    signatures.breeds = []

    # Assert
    assert False


def test_createemptysignatures():
    # Arrange
    signatures = Signatures()

    # Act
    signatures.createemptysignatures()

    # Assert
    assert False


def test_importsignatures_file():
    # Arrange
    # Act
    # Assert
    assert False


def test_importsignatures_string():
    # Arrange
    # Act
    # Assert
    assert False


def test_importsignatures_url():
    # Arrange
    # Act
    # Assert
    assert False


def test_exportsignatures_file():
    # Arrange
    # Act
    # Assert
    assert False


def test_exportsignatures_string():
    # Arrange
    # Act
    # Assert
    assert False


@pytest.mark.parametrize("input_data,result", [
    ("", False),
    ("", True)
])
def test_validatejsonsyntax(input_data, result):
    # Arrange
    signatures = Signatures()
    signatures.importsignatures(ImportTypes.STRING, input_data)

    # Act
    signatures.validatejsonsyntax()

    # Assert
    assert result


def test_jsontomodels():
    # Arrange
    # Act
    # Assert
    assert False


def test_modelstojson():
    # Arrange
    # Act
    # Assert
    assert False


def test_addosbreed():
    # Arrange
    # Act
    # Assert
    assert False


def test_addosversion():
    # Arrange
    signatures = Signatures()

    # Act
    signatures.addosbreed("Test")

    # Assert
    assert False


def test_removeosbreed():
    # Arrange
    # Act
    # Assert
    assert False


def test_removeosversion():
    # Arrange
    # Act
    # Assert
    assert False
