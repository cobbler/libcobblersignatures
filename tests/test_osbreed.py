import pytest

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


def test_osversion_no_name():
    with pytest.raises(TypeError) as e_info:
        OsBreed()


def test_osversions():
    # Arrange
    osbreed = OsBreed("test")

    # Act
    osbreed.supported_repo_breeds = []

    # Assert
    assert False


def test_osversion_add():
    # Arrange
    osbreed = OsBreed("test")

    # Act
    osbreed.osversion_add(Osversion(), 0)

    # Assert
    assert False


def test_osversion_remove():
    # Arrange
    osbreed = OsBreed("test")
    osbreed.osversion_add(Osversion(), 0)

    # Act
    osbreed.osversion_remove(0)

    # Assert
    assert False
