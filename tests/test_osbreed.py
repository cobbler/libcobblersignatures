import pytest

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


def test_osversion_no_name():
    with pytest.raises(TypeError) as e_info:
        OsBreed()


def test_name():
    # Arrange
    osbreed = OsBreed("test")

    # Act
    with pytest.raises(TypeError) as e_info:
        osbreed.name = ""


def test_osversion_add():
    # Arrange
    itemname = "test"
    osbreed = OsBreed(itemname)

    # Act
    osbreed.osversion_add(itemname, Osversion())

    # Assert
    assert itemname in osbreed.osversions


def test_osversion_remove():
    # Arrange
    itemname = "test"
    osbreed = OsBreed(itemname)
    osbreed.osversion_add(itemname, Osversion())

    # Act
    osbreed.osversion_remove(itemname)
