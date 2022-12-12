import pytest

from libcobblersignatures.models.osversion import Osversion
from tests.conftest import does_not_raise


def test_new_osversion():
    Osversion()


def test_osversion_equality():
    assert Osversion() == Osversion()


@pytest.mark.parametrize(
    "param,result,raises",
    [
        (
            {"RedHat/RPMS", "CentOS/RPMS"},
            {"RedHat/RPMS", "CentOS/RPMS"},
            does_not_raise(),
        ),
        ("", set(), pytest.raises(TypeError)),
    ],
)
def test_signatures(param, result, raises):
    # Arrange
    version = Osversion()

    # Act
    with raises:
        version.signatures = param

        # Assert
        assert version.signatures == result


def test_signatures_del():
    # Arrange
    version = Osversion()

    # Act
    del version.signatures

    # Assert
    assert version.signatures == set()


@pytest.mark.parametrize("param,result", [("", "")])
def test_version_file(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.version_file = param

    # Assert
    assert version.version_file == result


def test_version_file_del():
    # Arrange
    version = Osversion()

    # Act
    del version.version_file

    # Assert
    assert version.version_file == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_version_file_regex(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.version_file_regex = param

    # Assert
    assert version.version_file_regex == result


def test_version_file_regex_del():
    # Arrange
    version = Osversion()

    # Act
    del version.version_file_regex

    # Assert
    assert version.version_file_regex == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_kernel_arch(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.kernel_arch = param

    # Assert
    assert version.kernel_arch == result


def test_kernel_arch_del():
    # Arrange
    version = Osversion()

    # Act
    del version.kernel_arch

    # Assert
    assert version.kernel_arch == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_kernel_arch_regex(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.kernel_arch_regex = param

    # Assert
    assert version.kernel_arch_regex == result


def test_kernel_arch_regex_del():
    # Arrange
    version = Osversion()

    # Act
    del version.kernel_arch_regex

    # Assert
    assert version.kernel_arch_regex == ""


@pytest.mark.parametrize(
    "param,result",
    [
        ({"amd64", "i386"}, {"amd64", "i386"}),
        (["amd64", "i386", "amd64"], {"i386", "amd64"}),
    ],
)
def test_supported_arches(param, result):
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_arches = param

    # Assert
    assert osversion.supported_arches == result


def test_supported_arches_del():
    # Arrange
    version = Osversion()

    # Act
    del version.supported_arches

    # Assert
    assert version.supported_arches == set()


@pytest.mark.parametrize("param,result", [({"rhn", "apt"}, {"rhn", "apt"})])
def test_supported_repo_breeds(param, result):
    # Arrange
    osversion = Osversion()

    # Act
    osversion.supported_repo_breeds = param

    # Assert
    assert result


def test_supported_repo_breeds_del():
    # Arrange
    version = Osversion()

    # Act
    del version.supported_repo_breeds

    # Assert
    assert version.supported_repo_breeds == []


@pytest.mark.parametrize(
    "param,result,raises",
    [
        ("", "", does_not_raise()),
        (0, "", pytest.raises(TypeError)),
        ({}, "", pytest.raises(TypeError)),
        (None, "", pytest.raises(TypeError)),
        (False, "", pytest.raises(TypeError)),
        (["Element"], "", pytest.raises(TypeError)),
        ("ergodox", "ergodox", does_not_raise()),
    ],
)
def test_kernel_file(param, result, raises):
    # Arrange
    version = Osversion()

    # Act
    with raises:
        version.kernel_file = param

    # Assert
    assert version.kernel_file == result


def test_kernel_file_del():
    # Arrange
    version = Osversion()

    # Act
    del version.kernel_file

    # Assert
    assert version.kernel_file == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_initrd_file(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.initrd_file = param

    # Assert
    assert version.initrd_file == result


def test_initrd_file_del():
    # Arrange
    version = Osversion()

    # Act
    del version.initrd_file

    # Assert
    assert version.initrd_file == ""


@pytest.mark.parametrize(
    "param,result,raises",
    [
        ("", False, pytest.raises(TypeError)),
        (0, False, pytest.raises(TypeError)),
        ([], False, pytest.raises(TypeError)),
        ({}, False, pytest.raises(TypeError)),
        (True, True, does_not_raise()),
        (False, False, does_not_raise()),
    ],
)
def test_isolinux_ok(param, result, raises):
    # Arrange
    version = Osversion()

    # Act
    with raises:
        version.isolinux_ok = param

    # Assert
    assert version.isolinux_ok == result


def test_isolinux_ok_del():
    # Arrange
    version = Osversion()

    # Act
    del version.isolinux_ok

    # Assert
    assert not version.isolinux_ok


@pytest.mark.parametrize("param,result", [("", "")])
def test_default_autoinstall(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.default_autoinstall = param

    # Assert
    assert version.default_autoinstall == result


def test_default_autoinstall_del():
    # Arrange
    version = Osversion()

    # Act
    del version.default_autoinstall

    # Assert
    assert version.default_autoinstall == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_kernel_options(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.kernel_options = param

    # Assert
    assert version.kernel_options == result


def test_kernel_options_del():
    # Arrange
    version = Osversion()

    # Act
    del version.kernel_options

    # Assert
    assert version.kernel_options == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_kernel_options_post(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.kernel_options_post = param

    # Assert
    assert version.kernel_options_post == result


def test_kernel_options_post_del():
    # Arrange
    version = Osversion()

    # Act
    del version.kernel_options_post

    # Assert
    assert version.kernel_options_post == ""


@pytest.mark.parametrize("param,result", [("", "")])
def test_template_files(param, result):
    # Arrange
    version = Osversion()

    # Act
    version.template_files = param

    # Assert
    assert version.template_files == result


def test_template_files_del():
    # Arrange
    version = Osversion()

    # Act
    del version.template_files

    # Assert
    assert version.template_files == ""


@pytest.mark.parametrize(
    "param,result,raises",
    [
        ("", set(), pytest.raises(TypeError)),
        (0, set(), pytest.raises(TypeError)),
        ({}, set(), pytest.raises(TypeError)),
        (None, set(), pytest.raises(TypeError)),
        (False, set(), pytest.raises(TypeError)),
        (["Element"], {"Element"}, does_not_raise()),
        ({"Element"}, {"Element"}, does_not_raise()),
    ],
)
def test_boot_files(param, result, raises):
    # Arrange
    version = Osversion()

    # Act
    with raises:
        version.boot_files = param

        # Assert
        assert version.boot_files == result


def test_boot_files_del():
    # Arrange
    version = Osversion()

    # Act
    del version.boot_files

    # Assert
    assert version.boot_files == set()


@pytest.mark.parametrize(
    "param,result,raises",
    [
        ("", {}, pytest.raises(TypeError)),
        (0, {}, pytest.raises(TypeError)),
        (False, {}, pytest.raises(TypeError)),
        ([], {}, pytest.raises(TypeError)),
        (None, {}, pytest.raises(TypeError)),
        ({"Element": False}, {"Element": False}, does_not_raise()),
    ],
)
def test_boot_loaders(param, result, raises):
    # Arrange
    version = Osversion()

    # Act
    with raises:
        version.boot_loaders = param

    # Assert
    assert version.boot_loaders == result


def test_boot_loaders_del():
    # Arrange
    version = Osversion()

    # Act
    del version.boot_loaders

    # Assert
    assert version.boot_loaders == {}


def test_encode():
    # Arrange
    version = Osversion()

    # Act
    result = version.encode()

    # Assert
    assert isinstance(result, dict)
    # If we have an empty version, only the bools are shown.
    assert len(result) == 1


def test_encode_set():
    # Arrange
    version = Osversion()
    version.signatures.add("test")

    # Act
    result = version.encode()

    # Assert
    assert isinstance(result, dict)
    # If we have an empty version, only the bools are shown.
    assert len(result) == 2


def test_decode():
    # Arrange
    version = Osversion()
    data = {"version_file": "test"}

    # Act
    version.decode(data)

    # Assert
    assert version.version_file == "test"
