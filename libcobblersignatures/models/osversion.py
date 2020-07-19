from enum import Enum


class OsArchitectures(Enum):
    i386 = 1
    x86_64 = 2
    ppc = 3
    ppc64 = 4
    amd64 = 5


class RepositoryBreeds(Enum):
    rsync = 1
    rhn = 2
    yum = 3
    apt = 4


class Osversion:
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
    def signatures(self):
        return self._signatures

    @signatures.setter
    def signatures(self, value):
        self._signatures = value

    @signatures.deleter
    def signatures(self):
        del self._signatures

    @property
    def version_file(self):
        return self._version_file

    @version_file.setter
    def version_file(self, value):
        self._version_file = value

    @version_file.deleter
    def version_file(self):
        del self._version_file

    @property
    def version_file_regex(self):
        return self._version_file_regex

    @version_file_regex.setter
    def version_file_regex(self, value):
        self._version_file_regex = value

    @version_file_regex.deleter
    def version_file_regex(self):
        del self._version_file_regex

    @property
    def kernel_arch(self):
        return self._kernel_arch

    @kernel_arch.setter
    def kernel_arch(self, value):
        self._kernel_arch = value

    @kernel_arch.deleter
    def kernel_arch(self):
        del self._kernel_arch

    @property
    def kernel_arch_regex(self):
        return self._kernel_arch_regex

    @kernel_arch_regex.setter
    def kernel_arch_regex(self, value):
        self._kernel_arch_regex = value

    @kernel_arch_regex.deleter
    def kernel_arch_regex(self):
        del self._kernel_arch_regex

    @property
    def supported_arches(self):
        return self._supported_arches

    @supported_arches.setter
    def supported_arches(self, value):
        self._supported_arches = value

    @supported_arches.deleter
    def supported_arches(self):
        del self._supported_arches

    @property
    def supported_repo_breeds(self):
        return self._supported_repo_breeds

    @supported_repo_breeds.setter
    def supported_repo_breeds(self, value):
        self._supported_repo_breeds = value

    @supported_repo_breeds.deleter
    def supported_repo_breeds(self):
        del self._supported_repo_breeds

    @property
    def kernel_file(self):
        return self._kernel_file

    @kernel_file.setter
    def kernel_file(self, value):
        self._kernel_file = value

    @kernel_file.deleter
    def kernel_file(self):
        del self._kernel_file

    @property
    def initrd_file(self):
        return self._initrd_file

    @initrd_file.setter
    def initrd_file(self, value):
        self._initrd_file = value

    @initrd_file.deleter
    def initrd_file(self):
        del self._initrd_file

    @property
    def isolinux_ok(self):
        return self._isolinux_ok

    @isolinux_ok.setter
    def isolinux_ok(self, value):
        self._isolinux_ok = value

    @isolinux_ok.deleter
    def isolinux_ok(self):
        del self._isolinux_ok

    @property
    def default_autoinstall(self):
        return self._default_autoinstall

    @default_autoinstall.setter
    def default_autoinstall(self, value):
        self._default_autoinstall = value

    @default_autoinstall.deleter
    def default_autoinstall(self):
        del self._default_autoinstall

    @property
    def kernel_options(self):
        return self._kernel_options

    @kernel_options.setter
    def kernel_options(self, value):
        self._kernel_options = value

    @kernel_options.deleter
    def kernel_options(self):
        del self._kernel_options

    @property
    def kernel_options_post(self):
        return self._kernel_options_post

    @kernel_options_post.setter
    def kernel_options_post(self, value):
        self._kernel_options_post = value

    @kernel_options_post.deleter
    def kernel_options_post(self):
        del self._kernel_options_post

    @property
    def template_files(self):
        return self._template_files

    @template_files.setter
    def template_files(self, value):
        self._template_files = value

    @template_files.deleter
    def template_files(self):
        del self._template_files

    @property
    def boot_files(self):
        return self._boot_files

    @boot_files.setter
    def boot_files(self, value):
        self._boot_files = value

    @boot_files.deleter
    def boot_files(self):
        del self._boot_files

    @property
    def boot_loaders(self):
        return self._boot_loaders

    @boot_loaders.setter
    def boot_loaders(self, value):
        self._boot_loaders = value

    @boot_loaders.deleter
    def boot_loaders(self):
        del self._boot_loaders

    def encode(self):
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
