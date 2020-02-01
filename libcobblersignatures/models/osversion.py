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
        self._boot_files = []

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
    def boot_files(self):
        return self._boot_files

    @boot_files.setter
    def boot_files(self, value):
        self._boot_files = value

    @boot_files.deleter
    def boot_files(self):
        del self._boot_files
