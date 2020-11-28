from enum import Enum


class OsArchitectures(Enum):
    """
    An enumeration which defines the in Cobbler available architectures.
    """
    i386 = 1
    x86_64 = 2
    ppc = 3
    ppc64 = 4
    amd64 = 5


class RepositoryBreeds(Enum):
    """
    An enumeration which defines the in Cobbler available repository breeds.
    """
    rsync = 1
    rhn = 2
    yum = 3
    apt = 4


class Osversion:
    """
    A version of an operating system breed like ``openSUSE Leap 15.2``. The specification of the attributes and what
    values are valid are described in the JSON specification.
    """

    def __init__(self):
        self._signatures = []
        self._version_file = ""
        self._version_file_regex = ""
        self._kernel_arch = ""
        self._kernel_arch_regex = ""
        self._supported_arches = []
        self._supported_repo_breeds = []
        self._kernel_file = []
        self._initrd_file = ""
        self._isolinux_ok = False
        self._default_autoinstall = ""
        self._kernel_options = ""
        self._kernel_options_post = ""
        self._template_files = ""
        self._boot_files = []
        self._boot_loaders = {}

    def __eq__(self, other):
        if not isinstance(other, Osversion):
            return NotImplemented
        return self.signatures == other.signatures \
            and self.version_file == other.version_file \
            and self.version_file_regex == other.version_file_regex \
            and self.kernel_arch == other.kernel_arch \
            and self.kernel_arch_regex == other.kernel_arch_regex \
            and self.supported_arches == other.supported_arches \
            and self.supported_repo_breeds == other.supported_repo_breeds \
            and self.kernel_file == other.kernel_file \
            and self.initrd_file == other.initrd_file \
            and self.isolinux_ok == other.isolinux_ok \
            and self.default_autoinstall == other.default_autoinstall \
            and self.kernel_options == other.kernel_options \
            and self.kernel_options_post == other.kernel_options_post \
            and self.template_files == other._template_files \
            and self.boot_files == other.boot_files \
            and self.boot_loaders == other.boot_loaders

    @property
    def signatures(self) -> list:
        return self._signatures

    @signatures.setter
    def signatures(self, value: list):
        if isinstance(value, list):
            self._signatures = value
        else:
            raise TypeError("Signatures should be a list.")

    @signatures.deleter
    def signatures(self):
        self._signatures = []

    @property
    def version_file(self) -> str:
        return self._version_file

    @version_file.setter
    def version_file(self, value):
        if isinstance(value, str):
            self._version_file = value
        else:
            raise TypeError("The version_file should be a str.")

    @version_file.deleter
    def version_file(self):
        self._version_file = ""

    @property
    def version_file_regex(self) -> str:
        return self._version_file_regex

    @version_file_regex.setter
    def version_file_regex(self, value):
        if isinstance(value, str):
            self._version_file_regex = value
        else:
            raise TypeError("The version_file_regex should be a str.")

    @version_file_regex.deleter
    def version_file_regex(self):
        self._version_file_regex = ""

    @property
    def kernel_arch(self) -> str:
        return self._kernel_arch

    @kernel_arch.setter
    def kernel_arch(self, value):
        if isinstance(value, str):
            self._kernel_arch = value
        else:
            raise TypeError("The kernel_arch should be a str.")

    @kernel_arch.deleter
    def kernel_arch(self):
        self._kernel_arch = ""

    @property
    def kernel_arch_regex(self) -> str:
        return self._kernel_arch_regex

    @kernel_arch_regex.setter
    def kernel_arch_regex(self, value):
        if isinstance(value, str):
            self._kernel_arch_regex = value
        else:
            raise TypeError("The kernel_arch_regex should be a str.")

    @kernel_arch_regex.deleter
    def kernel_arch_regex(self):
        self._kernel_arch_regex = ""

    @property
    def supported_arches(self) -> list:
        return self._supported_arches

    @supported_arches.setter
    def supported_arches(self, value):
        if isinstance(value, list):
            self._supported_arches = value
        else:
            raise TypeError("The supported_arches should be a list.")

    @supported_arches.deleter
    def supported_arches(self):
        self._supported_arches = []

    @property
    def supported_repo_breeds(self) -> list:
        return self._supported_repo_breeds

    @supported_repo_breeds.setter
    def supported_repo_breeds(self, value):
        if isinstance(value, list):
            self._supported_repo_breeds = value
        else:
            raise TypeError("The supported_repo_breeds should be a list.")

    @supported_repo_breeds.deleter
    def supported_repo_breeds(self):
        self._supported_repo_breeds = []

    @property
    def kernel_file(self) -> list:
        return self._kernel_file

    @kernel_file.setter
    def kernel_file(self, value):
        if isinstance(value, list):
            self._kernel_file = value
        else:
            raise TypeError("The kernel_file should be a list.")

    @kernel_file.deleter
    def kernel_file(self):
        self._kernel_file = []

    @property
    def initrd_file(self) -> str:
        return self._initrd_file

    @initrd_file.setter
    def initrd_file(self, value):
        if isinstance(value, str):
            self._initrd_file = value
        else:
            raise TypeError("The initrd_file should be a str.")

    @initrd_file.deleter
    def initrd_file(self):
        self._initrd_file = ""

    @property
    def isolinux_ok(self) -> bool:
        return self._isolinux_ok

    @isolinux_ok.setter
    def isolinux_ok(self, value):
        if isinstance(value, bool):
            self._isolinux_ok = value
        else:
            raise TypeError("The isolinux_ok should be a bool.")

    @isolinux_ok.deleter
    def isolinux_ok(self):
        self._isolinux_ok = False

    @property
    def default_autoinstall(self):
        return self._default_autoinstall

    @default_autoinstall.setter
    def default_autoinstall(self, value):
        self._default_autoinstall = value

    @default_autoinstall.deleter
    def default_autoinstall(self):
        self._default_autoinstall = ""

    @property
    def kernel_options(self) -> str:
        return self._kernel_options

    @kernel_options.setter
    def kernel_options(self, value):
        self._kernel_options = value

    @kernel_options.deleter
    def kernel_options(self):
        self._kernel_options = ""

    @property
    def kernel_options_post(self) -> str:
        return self._kernel_options_post

    @kernel_options_post.setter
    def kernel_options_post(self, value):
        if isinstance(value, str):
            self._kernel_options_post = value
        else:
            raise TypeError("The kernel_options_post should be a str.")

    @kernel_options_post.deleter
    def kernel_options_post(self):
        self._kernel_options_post = ""

    @property
    def template_files(self) -> str:
        return self._template_files

    @template_files.setter
    def template_files(self, value):
        if isinstance(value, str):
            self._template_files = value
        else:
            raise TypeError("The template_files should be a str.")

    @template_files.deleter
    def template_files(self):
        self._template_files = ""

    @property
    def boot_files(self) -> list:
        return self._boot_files

    @boot_files.setter
    def boot_files(self, value):
        if isinstance(value, list):
            self._boot_files = value
        else:
            raise TypeError("The boot_files should be a list.")

    @boot_files.deleter
    def boot_files(self):
        self._boot_files = []

    @property
    def boot_loaders(self) -> dict:
        return self._boot_loaders

    @boot_loaders.setter
    def boot_loaders(self, value):
        if isinstance(value, dict):
            self._boot_loaders = value
        else:
            raise TypeError("The boot_loaders should be a dict.")

    @boot_loaders.deleter
    def boot_loaders(self):
        self._boot_loaders = {}

    def encode(self) -> dict:
        """
        Encodes a single :class:`Osversion`. This means that the properties of an object is transferred into a JSON.

        :return: The dictionary with the data.
        """
        return {
            "signatures": self.signatures,
            "version_file": self.version_file,
            "version_file_regex": self.version_file_regex,
            "kernel_arch": self.kernel_arch,
            "kernel_arch_regex": self.kernel_arch_regex,
            "supported_arches": self.supported_arches,
            "supported_repo_breeds": self.supported_repo_breeds,
            "kernel_file": self.kernel_file,
            "initrd_file": self.initrd_file,
            "isolinux_ok": self.isolinux_ok,
            "default_autoinstall": self.default_autoinstall,
            "kernel_options": self.kernel_options,
            "kernel_options_post": self.kernel_options_post,
            "template_files": self._template_files,
            "boot_files": self.boot_files,
            "boot_loaders": self.boot_loaders
        }

    def decode(self, data):
        """
        Decodes the received data. This means parsing each attribute from the JSON into the property of an object.

        :param data: The data to decode.
        """
        self.signatures = data.get("signatures", [])
        self.version_file = data.get("version_file", "")
        self.version_file_regex = data.get("version_file_regex", "")
        self.kernel_arch = data.get("kernel_arch", "")
        self.kernel_arch_regex = data.get("kernel_arch_regex", "")
        self.supported_arches = data.get("supported_arches", [])
        self.supported_repo_breeds = data.get("supported_repo_breeds", [])
        self.kernel_file = data.get("kernel_file", [])
        self.initrd_file = data.get("initrd_file", "")
        self.isolinux_ok = data.get("isolinux_ok", False)
        self.default_autoinstall = data.get("default_autoinstall", "")
        self.kernel_options = data.get("kernel_options", "")
        self.kernel_options_post = data.get("kernel_options_post", "")
        self.template_files = data.get("template_files", "")
        self.boot_files = data.get("boot_files", [])
        self.boot_loaders = data.get("boot_loaders", {})
