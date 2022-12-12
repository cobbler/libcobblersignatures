from json.decoder import JSONDecodeError
import pytest

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion
from libcobblersignatures.enums import ImportTypes, ExportTypes
from libcobblersignatures import Signatures

from tests.conftest import does_not_raise


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
    testdata = '{"breeds": {}}'
    expected = {"breeds": {}}
    create_signatures_json(testdata)
    os_signatures = Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.FILE, testpath)

    # Assert
    assert expected == os_signatures.signaturesjson


def test_importsignatures_string():
    # Arrange
    signatures_text = '{"breeds": {}}'
    os_signatures = Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.STRING, signatures_text)

    # Assert
    # Currently we cannot check this any further but we will need additional checks for that.
    assert True


def test_importsignatures_url():
    # Arrange
    url = "https://cobbler.github.io/signatures/latest.json"
    os_signatures = Signatures()

    # Act
    os_signatures.importsignatures(ImportTypes.URL, url)

    # Assert
    # Currently we cannot check this any further but we will need additional checks for that.
    assert True


def test_importsignatures_unkown():
    # Arrange
    os_signatures = Signatures()

    # Act & Assert
    with pytest.raises(ValueError):
        os_signatures.importsignatures(100, "")


def test_export_missing_rootkey():
    # Arrange
    os_signatures = Signatures()
    os_signatures.importsignatures(ImportTypes.STRING, "{}")

    # Act & Assert
    with pytest.raises(AttributeError):
        os_signatures.jsontomodels()


@pytest.mark.usefixtures("delete_signatures_json")
def test_exportsignatures_file(testpath):
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("suse")
    expected = '{"breeds": {"suse": {}}}'

    # Act
    os_signatures.exportsignatures(ExportTypes.FILE, testpath)
    with open(testpath, "r") as f:
        result = f.read()

    # Assert
    assert expected == result


def test_exportsignatures_file_nopath():
    # Arrange
    os_signatures = Signatures()
    os_signatures.importsignatures(ImportTypes.STRING, '{"breeds": {}}')

    # Act & Assert
    with pytest.raises(ValueError):
        os_signatures.exportsignatures(ExportTypes.FILE)


def test_exportsignatures_string():
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("suse")
    expected = '{"breeds": {"suse": {}}}'

    # Act
    result = os_signatures.exportsignatures(ExportTypes.STRING)

    # Assert
    assert expected == result


def test_exportsignatures_unkown():
    # Arrange
    os_signatures = Signatures()
    os_signatures.importsignatures(ImportTypes.STRING, '{"breeds": {}}')

    # Act & Assert
    with pytest.raises(ValueError):
        os_signatures.exportsignatures(100)


@pytest.mark.parametrize(
    "input_data,result,raises",
    [
        ('{"breeds; {}}', {}, pytest.raises(JSONDecodeError)),
        ('{"breeds": {}}', {"breeds": {}}, does_not_raise()),
    ],
)
def test_signaturesjson(input_data, result, raises):
    # Arrange
    os_signatures = Signatures()
    with raises:
        os_signatures.importsignatures(ImportTypes.STRING, input_data)

        # Act
        os_signatures.signaturesjson = input_data

    # Assert
    assert result == os_signatures.signaturesjson


@pytest.mark.parametrize(
    "input_data,expected_data",
    [('{"breeds": {}}', []), ('{"breeds": {"suse": {}}}', [OsBreed("suse")])],
)
def test_jsontomodels(input_data, expected_data):
    # Arrange
    os_signatures = Signatures()
    os_signatures.importsignatures(ImportTypes.STRING, input_data)

    # Act
    os_signatures.jsontomodels()

    # Assert
    assert expected_data == os_signatures.osbreeds


def test_addosbreed():
    # Arrange
    os_signatures = Signatures()

    # Act
    os_signatures.addosbreed("Test")

    # Assert
    assert len(os_signatures.osbreeds) == 1


def test_addosversion():
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("suse")

    # Act
    os_signatures.addosversion(0, "sles", Osversion())

    # Assert
    assert os_signatures.osbreeds[0].osversions["sles"] == Osversion()


def test_addosversion_empty():
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("suse")

    # Act
    os_signatures.addosversion(0, "sles", None)

    # Assert
    assert os_signatures.osbreeds[0].osversions["sles"] == Osversion()


def test_removeosbreed():
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("Test")
    len_before = len(os_signatures.osbreeds)

    # Act
    os_signatures.removeosbreed(0)
    len_after = len(os_signatures.osbreeds)

    # Assert
    assert len_before == 1
    assert len_after == 0


def test_removeosversion():
    # Arrange
    os_signatures = Signatures()
    os_signatures.addosbreed("suse")
    os_signatures.addosversion(0, "sles", Osversion())

    # Act
    os_signatures.removeosversion(0, "sles")

    # Assert
    assert os_signatures.osbreeds[0].osversions == {}


def test_removeosversion_outofbounds():
    # Arrange
    os_signatures = Signatures()

    # Act & Assert
    with pytest.raises(ValueError):
        os_signatures.removeosbreed(1)


def test_get_breed_index_by_name():
    # Arrange
    os_signatures = Signatures()
    name_to_get = "suse"
    os_signatures.addosbreed(name_to_get)

    # Act
    result = os_signatures.get_breed_index_by_name(name_to_get)

    # Assert
    assert result == 0


def test_get_breed_index_by_name_not_existent():
    # Arrange
    os_signatures = Signatures()

    # Act
    result = os_signatures.get_breed_index_by_name("redhat")

    # Assert
    assert result == -1
