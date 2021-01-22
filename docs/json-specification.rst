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

The object has the following keys (type included):

+---------------------------+------------------+-------------+
| Name                      | Type             | Description |
+---------------------------+------------------+-------------+
| ``signatures``            | Array of Strings |             |
+---------------------------+------------------+-------------+
| ``version_file``          | String           |             |
+---------------------------+------------------+-------------+
| ``version_file_regex``    | String           |             |
+---------------------------+------------------+-------------+
| ``kernel_arch``           | String           |             |
+---------------------------+------------------+-------------+
| ``kernel_arch_regex``     | String           |             |
+---------------------------+------------------+-------------+
| ``supported_arches``      | Array of Strings |             |
+---------------------------+------------------+-------------+
| ``supported_repo_breeds`` | Array of Strings |             |
+---------------------------+------------------+-------------+
| ``kernel_file``           | String           |             |
+---------------------------+------------------+-------------+
| ``initrd_file``           | String           |             |
+---------------------------+------------------+-------------+
| ``isolinux_ok``           | Boolean          |             |
+---------------------------+------------------+-------------+
| ``default_autoinstall``   | String           |             |
+---------------------------+------------------+-------------+
| ``kernel_options``        | String           |             |
+---------------------------+------------------+-------------+
| ``kernel_options_post``   | String           |             |
+---------------------------+------------------+-------------+
| ``template_files``        | String           |             |
+---------------------------+------------------+-------------+
| ``boot_files``            | Array of Strings |             |
+---------------------------+------------------+-------------+
| ``boot_loaders``          | Dictionary       |             |
+---------------------------+------------------+-------------+

.. note:
   The current json type ``null`` is not valid in our context. Please use empty string, list or dicts for default
   values.

Example files
#############

Please have a look at https://github.com/cobbler/cobbler/blob/master/config/cobbler/distro_signatures.json

The most simple valid (but useless) ``signatures.json`` file will be:

.. code-block:: json

   {
     "breeds": {}
   }
