import pytest

from libcobblersignatures.models.osversion import Osversion


def test_new_osversion():
    Osversion()


def test_osversion_equality():
    assert Osversion() == Osversion()


@pytest.mark.parametrize("param,result", [
    (["amd64", "i386"], ["amd64", "i386"])
])
def test_supported_arches(param, result):
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_arches = param

    # Assert
    assert osversion.supported_arches == result


@pytest.mark.parametrize("param,result", [
    (["rhn", "apt"], ["rhn", "apt"])
])
def test_supported_repo_breeds(param, result):
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_repo_breeds = param

    # Assert
    assert result
