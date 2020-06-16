import pytest

from libcobblersignatures import signatures
from libcobblersignatures.signatures import Signatures, ImportTypes, ExportTypes


def test_breeds():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.osbreeds = []

    # Assert
    assert [] == os_signatures.osbreeds


@pytest.mark.usefixtures("delete_signatures_json")
def test_importsignatures_file(create_signatures_json, testpath):
    # Arrange
    expected = ""
    create_signatures_json(expected)
    os_signatures = signatures.Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.FILE, testpath)

    # Assert
    assert expected == os_signatures.signaturesjson


def test_importsignatures_string():
    # Arrange
    signatures_text = "{\"breeds\": {}}"
    os_signatures = signatures.Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.STRING, signatures_text)

    # Assert
    # Currently we cannot check this any further but we will need additional checks for that.
    assert True


def test_importsignatures_url():
    # Arrange
    url = "https://cobbler.github.io/signatures/latest.json"
    os_signatures = signatures.Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.URL, url)

    # Assert
    # Currently we cannot check this any further but we will need additional checks for that.
    assert True


@pytest.mark.usefixtures("delete_signatures_json")
def test_exportsignatures_file(testpath):
    # Arrange
    os_signatures = Signatures()
    expected = "{\"breeds\": {}"

    # Act
    os_signatures.exportsignatures(ExportTypes.FILE, testpath)
    with open(testpath, "r") as f:
        result = f.read()

    # Assert
    assert expected == result


def test_exportsignatures_string():
    # Arrange
    os_signatures = Signatures()
    expected = "{\"breeds\": {}"

    # Act
    result = os_signatures.exportsignatures(ExportTypes.STRING)

    # Assert
    assert expected == result


@pytest.mark.parametrize("input_data,result", [
    ("{\"breeds; {}}", None),
    ("{\"breeds\": {}}", "{\"breeds\": {}}")
])
def test_signaturesjson(input_data, result):
    # Arrange
    os_signatures = Signatures()
    os_signatures.importsignatures(ImportTypes.STRING, input_data)

    # Act
    os_signatures.signaturesjson = input_data

    # Assert
    assert result == os_signatures.signaturesjson


def test_jsontomodels():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.jsontomodels()

    # Assert
    assert False


def test_modelstojson():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.modelstojson()

    # Assert
    assert False


def test_addosbreed():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.addosbreed("Test")

    # Assert
    assert False


def test_addosversion():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.addosversion()

    # Assert
    assert False


def test_removeosbreed():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.removeosbreed("Test")

    # Assert
    assert False


def test_removeosversion():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.removeosversion()

    # Assert
    assert False
