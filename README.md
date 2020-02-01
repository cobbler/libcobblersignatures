# libcobblersignatures

This library should be the interface for all applications using cobbler signatures.

## Features

- Create a cobbler signatures document from scratch
- Modify existing cobbler signature documents
- Read cobbler signatures document
- Hand over structured data to other applications

## Signatures-JSON Specification

### Goal

This file should be the data which is used by a program to detect with a general algorithm which operating system an iso
image is handed to the program. This specification should not limit itself to one operating system but if this is not
possible then we shall focus on Linux and it's Distributions.

### File structure

The file should be a single JSON Object which has a single key with the name `breeds`. This key should contain a single
subobject with key-value pairs for each operating system group.

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

Each of these operating system groups has a key for each version of it. The key should be in lowercase and should have
a versionsuffix. The name of the key should be unique across the distro section.

The Key contains an object which has the following keys (type inclueded):

- signatures - Array
- version_file - String 
- version_file_regex - String
- kernel_arch - String
- kernel_arch_regex - String
- supported_arches - Array of Strings
- supported_repo_breeds - Array of Strings
- kernel_file - String
- initrd_file - String
- isolinux_ok - Boolean
- default_autoinstall - String
- kernel_options - String
- kernel_options_post - String
- boot_files - Array

### Example file

Please have a look at https://github.com/cobbler/cobbler/blob/master/config/cobbler/distro_signatures.json  
