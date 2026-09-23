Adding a New Distribution to distro_signatures.json
===================================================

This document explains how to collect the values needed to add a new
distribution to ``distro_signatures.json``.


Step 1: Download the ISO
------------------------

Download the installation ISO of the distribution you want to add and save it
locally.


Step 2: Mount the ISO
---------------------

Mounting the ISO in a loop device is the recommended way, because it only
needs the onboard tools of Linux and makes all files inside the ISO
accessible like a normal folder. First create a directory to mount the ISO to:

.. code-block:: bash

   sudo mkdir -p /mnt/iso

Then mount the ISO:

.. code-block:: bash

   sudo mount -o loop /path/to/your/image.iso /mnt/iso

The following steps use ``find`` and ``cat`` on the mounted ISO.

Alternative: 7-Zip
""""""""""""""""""
If you cannot mount the ISO, install 7-Zip
instead (the package name may vary between distributions):

.. code-block:: bash

   sudo apt install p7zip-full

7-Zip lets you inspect and read files inside the ISO without mounting it.
Each of the following steps shows the 7-Zip equivalent command as well.


Step 3: Find ``kernel_file`` and ``initrd_file``
------------------------------------------------

.. code-block:: bash

   find /mnt/iso | grep -E "vmlinuz|initrd"

This shows the boot kernel and its initrd, which are usually in the same
folder. Typical locations (not necessarily) are:

- Most RPM-based distros: ``/isolinux/vmlinuz`` and ``initrd.img``
- Debian: ``/images/pxeboot/``
- Ubuntu: ``casper/vmlinuz``
- SUSE: ``boot/<arch>/loader/``

.. note::

   For SUSE ISO's:
   The ``kernel_file`` is next to the ``initrd_file``

   .. code-block::

      ls /path/to/initrd

   For Debian ISO's:
   There are a lot of cluttered files after running the command,
   you can ignore: ``gtk, xen, udeb``, as you only need text-based installer files.

.. note::
   Look at the output of your find command and drop the directory paths.

   - If ``find`` gave you /casper/initrd.lz, your base name is initrd.lz.

   - If ``find`` gave you /install/vmlinuz-5.14.0, your base name is vmlinuz-5.14.0.

   .. admonition:: formatting the base name to python

      For the Kernel (kernel_file):
      Append (.*) to account for potential suffixes:

          ``vmlinuz-5.14.0 -> "vmlinuz(.*)"``

          ``linux -> "linux(.*)"``

      For the Initrd (initrd_file):
      Because initrd files have various extensions (.img, .gz, .lz, .xz), you must double-escape the regex dot character ``(\\.)``.

          ``initrd.img -> "initrd(.*)\\.img"``

          ``initrd.gz -> "initrd(.*)\\.gz"``

**7-Zip alternative:**

.. code-block:: bash

   7z l image.iso | grep -E "vmlinuz|initrd"

Step 4: Check for ``isolinux``
------------------------------

This checks whether ``/isolinux/isolinux.bin`` and ``isolinux.cfg`` both
exist. If both are present, isolinux is supported.

.. code-block:: bash

   find /mnt/iso -name "isolinux*"

.. note::

   isolinux is disabled most of the time

**7-Zip alternative:**

.. code-block:: bash

   7z l image.iso | grep isolinux


Step 5: Find the ``version_file`` and ``supported_arches``
----------------------------------------------------------

.. code-block:: bash

   find /mnt/iso \( -name ".treeinfo" -o -name ".discinfo" -o -path "*/.disk/info" \)

This shows which version file exists in the ISO. Use the matching file as
your ``version_file``.

Replace ``.treeinfo`` below with the file you found above:

.. code-block:: bash

   cat /mnt/iso/.treeinfo

This prints the file in readable form. The line ``arch =`` gives your
``supported_arches`` (``.treeinfo``).

.. note::

   For Debian/Ubuntu, the architecture is part of the ``.disk/info`` line.

If the version cannot be read: some distributions do
not ship a file with a fixed name or format. In this case use the
``version_file_regex`` key, a regular expression that is applied to the
``version_file`` to extract the version.


.. note::
   version_file tells Cobbler which file to open and read.

   version_file_regex tells Cobbler how to read the text inside that file to extract only the version number.

   check ``vmware, freebsd, xen`` for reference

**7-Zip alternative:**

.. code-block:: bash

   7z l image.iso | grep -E "\.treeinfo|\.discinfo|\.disk/info"

Then extract the file and read it:

.. code-block:: bash

   7z x image.iso .treeinfo -oextracted
   cat extracted/.treeinfo

The first command extracts only that file into a folder called
``extracted``, without a space between ``-o`` and ``extracted``. The second
prints the file in readable form.

.. note::

   If ``7z x`` prints nothing, the file is probably not at the ISO root, or
   the path does not match exactly. Paths are case-sensitive and must not
   start with ``/``, so check the exact path with the ``7z l`` command above.


Step 6: Determine ``supported_repo_breeds``
-------------------------------------------

.. code-block:: bash

   find /mnt/iso -maxdepth 3 \( -name "repodata" -o -name "dists" -o -name "content" \)

This shows which kind of repository metadata the ISO ships. Match the result
to the repo breed:

- **yum:** ``repodata/`` with ``repomd.xml``
- **apt:** ``dists/<name>/`` with ``Packages.gz`` and ``Release``
- **zypper:** ``repodata/`` with a ``content`` file

.. note::

   some distributions don't have a ``supported_repo_breed``

**7-Zip alternative:**

.. code-block:: bash

   7z l image.iso | grep -E "repodata|dists|repomd|content|Release|Packages.gz"


Step 7: Determine the remaining properties
------------------------------------------

The following properties complete the entry.

``default_autoinstall``
"""""""""""""""""""""""

The default_autoinstall key is completely optional in a Cobbler signature.
If an entry in ``distro_signatures.json`` does not have it,
it simply means Cobbler will not automatically attach a kickstart/preseed/AutoYaST template,
when you import that specific ISO.

.. note::
   Debian and Legacy Ubuntu use Preseed:
   "sample.seed"

   Modern Ubuntu use Subiquity (Cloud-init):
   "sample_autoinstall_meta.yaml"

   openSUSE and SLES use AutoYaST:
   "sample_autoyast.xml"

   Legacy Red Hat Family use Legacy Kickstart:
   "sample_legacy.ks"

   Modern Red Hat Family use Kickstart.
   "sample.ks"

   VMware ESXi uses its own kickstart format:
   "sample_esxi(insert version-number).ks"

   Xen/XCP-ng uses:
   "answerfile.xml"

   windows uses:
   "win.ks"

   powerkvm uses:
   "powerkvm.ks"

``kernel_arch``
"""""""""""""""

A file name or pattern that identifies the architecture of the
distribution.

RPM-based distros usually use the kernel package, ``kernel-(.*).rpm``.

.. code-block:: bash

   find /mnt/iso -name "kernel-*.rpm"

Debian based distros usually use the header package, ``linux-headers-(.*)\\.deb``

.. code-block:: bash

   grep -r /mnt/iso -name "linux-headers-"

Checks that such a file exists in the ISO.

.. note::

   kernel_arch (if specified) hardcodes the system architecture (e.g., x86_64, i386).

   kernel_arch_regex tells Cobbler how to extract the architecture from the file path or filename of the kernel.
   It extracts the architecture.

   check ``vmware, freebsd, xen`` for reference and use either of the commands above to double check.

**7-Zip alternative:**

.. code-block::

   7z l image.iso | grep "kernel-"

``kernel_options``
""""""""""""""""""
Kernel options that are always passed when booting the
installer. Leave it empty (``""``) if none are needed.

``kernel_options_post``
"""""""""""""""""""""""
Additional kernel options that are applied to the installed system
after the installation. Leave it empty (``""``) in most cases.

``boot_files and boot_loaders``
"""""""""""""""""""""""""""""""
A list of files that are added to the ``boot_files`` of the
imported distribution.

Cobbler provides its own PXE bootloader (pxelinux.0 or GRUB) and its own boot menus.
It usually only needs the ``kernel_file`` and ``initrd_file`` from the ISO to make the OS boot.

In most cases ``boot_files`` is left empty (``[]``).
``esxi5`` uses ``["*.*"]`` to copy all files of the ISO.

As long as no specific bootloader is desired, ``{}`` is used to make it boot via global defaults.

Step 8: Add the entry to ``distro_signatures.json``
---------------------------------------------------

Open the file and add a new entry for the distribution, filling in the
values collected in Steps 3-7. Place it under the correct breed and keep
the same structure as the existing entries.


Step 9: Unmount the ISO
-----------------------

.. code-block:: bash

   sudo umount /mnt/iso

This releases the loop mount once you have collected all values.

Not needed when using 7-Zip.
