************************************
Specification of ``signatures.json``
************************************

Goal
####

This file should contain the data which is used by a program to recognize with a general algorithm which operating
system an ISO image passes to the program. This specification should not be limited itself to one operating system. If
that this is not possible, we shall focus on Linux and its distributions.

File structure
##############

The file should be a single JSON object which has a single key with the name `breeds`. This key should contain a single
sub-object with key-value pairs for each operating system group.

Currently the following operating system groups are existing:

- redhat
- debian
- ubuntu
- suse
- vmware
- freebsd
- xen
- unix
- windows
- powerkvm
- generic

This list should be modified when new groups are added, removed or changed when changed in the JSON.

Each of these operating system groups have a key for each version of it. The key should be in lowercase and should have
a version suffix. The name of the key should be unique across the distribution section and contains an object.

For a list of keys and types please look at our schema:
https://github.com/cobbler/libcobblersignatures/tree/main/docs/schema.json

.. note::
   The schema is used to validate the signatures and can be used as a template for writing and comparing
   your own signatures. For more information read the JSON Schema documentation at https://json-schema.org/

.. note::
    The current json type ``null`` is only valid for ``version_file_regex`` and ``kernel_arch_regex``.
    For all other keys please use empty strings, lists or dicts for default values.

Version keys
############

Each operating system version object supports the following keys. This table is generated from
the docstrings of :class:`libcobblersignatures.models.osversion.Osversion` by
``scripts/sync_json_spec_docs.py`` — update the docstrings, then re-run the script, rather than
editing the table below directly.

.. sync-json-spec-docs: start

.. list-table:: ``signatures.json`` version keys
   :header-rows: 1

   * - Key
     - Type
     - Description
   * - ``signatures``
     - array
     - One or more paths, relative to the root of the ISO, whose existence identifies this OS version.
   * - ``version_file``
     - string / null
     - The regular expression which points to the file with the os-version info.
   * - ``version_file_regex``
     - string / null
     - The regular expression matched against the contents of the file located via ``version_file`` to confirm this version.
   * - ``kernel_arch``
     - string
     - The regular expression which tells Cobbler where to look for the architecture of the operating system. In some cases this may also be a path to the file where Cobbler should look for the architecture.
   * - ``kernel_arch_regex``
     - string / null
     - The regex applied within the file located via ``kernel_arch`` when it doesn't point to the architecture directly.
   * - ``supported_arches``
     - array
     - The architectures Cobbler considers valid when detecting the architecture of an imported distro.
   * - ``supported_repo_breeds``
     - array
     - The repository breeds Cobbler may auto-create when it finds a matching repo in the install tree.
   * - ``kernel_file``
     - string
     - The regular expression to match to find the kernel.
   * - ``initrd_file``
     - string
     - The regular expression to match to find the initrd.
   * - ``isolinux_ok``
     - boolean
     - Whether directories named ``isolinux`` should still be scanned for a kernel/initrd pair instead of being skipped.
   * - ``default_autoinstall``
     - string
     - The filename for the default autoinstall template in Cobbler.
   * - ``kernel_options``
     - string
     - Default kernel options to apply to the imported ISO.
   * - ``kernel_options_post``
     - string
     - Default kernel post options to apply to the imported ISO.
   * - ``template_files``
     - string
     - Extra files merged into the imported distro's template_files, used to render templated boot files (e.g. ESXi's boot.cfg).
   * - ``boot_files``
     - array
     - Extra files, beyond the kernel and initrd, that must be copied out of the source tree and templated for the distro.
   * - ``boot_loaders``
     - object
     - The boot loaders Cobbler considers valid for this OS version, keyed by architecture.

.. sync-json-spec-docs: end

Example files
#############

Please have a look at
https://github.com/cobbler/libcobblersignatures/tree/main/libcobblersignatures/config/distro_signatures.json

The most simple valid (but useless) ``signatures.json`` file will be:

.. code-block:: json

   {
     "breeds": {}
   }
