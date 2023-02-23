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

Example files
#############

Please have a look at
https://github.com/cobbler/libcobblersignatures/tree/main/libcobblersignatures/config/distro_signatures.json

The most simple valid (but useless) ``signatures.json`` file will be:

.. code-block:: json

   {
     "breeds": {}
   }
