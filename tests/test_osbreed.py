import collections

import pytest

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


def test_osbreed_equality():
    # Arrange, Act & Assert
    assert OsBreed("test") == OsBreed("test")


def test_osbreed_non_equality():
    # Arrange, Act & Assert
    assert not OsBreed("test") == Osversion()


def test_breed_no_name():
    # Arrange, Act & Assert
    with pytest.raises(TypeError) as e_info:
        OsBreed()


def test_name():
    # Arrange
    osbreed = OsBreed("test")

    # Act
    osbreed.name = "Test"

    # Assert
    osbreed.name = "Test"


def test_name_empty():
    # Arrange
    osbreed = OsBreed("test")

    # Act & Assert
    with pytest.raises(TypeError) as e_info:
        osbreed.name = ""


def test_name_delete():
    # Arrange
    osbreed = OsBreed("test")

    # Act & Assert
    with pytest.raises(TypeError):
        del osbreed.name
    assert osbreed.name == "test"


def test_osversions():
    # Arrange
    osbreed = OsBreed("suse")
    new_value = []

    # Act & Assert
    with pytest.raises(TypeError):
        osbreed.osversions = new_value
    assert isinstance(osbreed._osversions, collections.OrderedDict)


def test_osversions_delete():
    # Arrange
    osbreed = OsBreed("suse")

    # Act
    osbreed.osversion_add("susesp1", Osversion())
    del osbreed.osversions

    # Arrange
    assert osbreed.osversions == collections.OrderedDict()


def test_breed_add():
    # Arrange
    itemname = "test"
    osbreed = OsBreed(itemname)

    # Act
    osbreed.osversion_add(itemname, Osversion())

    # Assert
    assert itemname in osbreed.osversions


def test_breed_add_type_error():
    # Arrange
    osbreed = OsBreed("test")

    # Act & Arrange
    with pytest.raises(ValueError):
        osbreed.osversion_add(0, "")


def test_breed_remove():
    # Arrange
    itemname = "test"
    osbreed = OsBreed(itemname)
    osbreed.osversion_add(itemname, Osversion())

    # Act & Assert
    osbreed.osversion_remove(itemname)


def test_encode():
    # Arrange
    breed = OsBreed("test")
    breed.osversion_add("test1", Osversion())
    breed.osversion_add("test2", Osversion())

    # Act
    result = breed.encode()

    # Assert
    assert isinstance(result, dict)
    assert "test1" in result
    assert "test2" in result
    assert isinstance(result["test1"], dict)


def test_decode():
    # Arrange
    breed = OsBreed("test")
    data = {"version1": {}, "version2": {}}

    # Act
    breed.decode(data)

    # Assert
    assert breed.osversions["version1"]
    assert breed.osversions["version2"]
