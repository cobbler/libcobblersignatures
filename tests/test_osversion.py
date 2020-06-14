from libcobblersignatures.models.osversion import Osversion


def test_new_osversion():
    Osversion()


def test_supported_arches():
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_arches = []

    # Assert
    assert False


def test_supported_repo_breeds():
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_repo_breeds = []

    # Assert
    assert False
