How to figure out the distro_signatures.json fields.
================================================


``kernel_file / initrd_file``
    The boot kernel and its initrd can be found here. They usally are in
    the same folder:

    - ``/isolinux/vmlinuz`` + ``initrd.img`` on most RPM
    - ``/images/pxeboot/``
    - ``casper/vmlinuz`` on Ubuntu
    - ``boot/<arch>/loader/`` on SUSE


``isolinux``
    Check if ``/isolinux/isolinux.bin`` and ``isolinux.cfg`` exist.

``version_file``
    can be found here (``7z x image.iso -so /path/within/iso``):

    - Fedora/RHEL/CentOS/Rocky/Alma -> ``.treeinfo`` or ``.discinfo``

    - Debian/Ubuntu -> ``.disk/info``

    - openSUSE/SLES -> ``install/x86_64``

    - old Fedora -> ``media.repo``

``supported_arches``
    Easiest source is ``.treeinfo``, under ``[general] arch =``

    Otherwise look at the directory names, x86_64 / aarch64 / i386 etc

    Debian puts this in .disk/info

``supported_repo_breeds``
    Depends what kind of repo metadata the ISO ships:

    - redhat: repodata/ + repomd.xml -> yum

    - debian/ubuntu: dists/<name>/`` with Packages.gz/Release -> apt

    - suse: repodata/content layout -> zypper