**********************
Command Line Interface
**********************

The CLI is reachable via the command ``cobbler-manage-signatures``. After that you are in an interactive session. This
session does not save anything except you explicitly tell the CLI to do so.

The top-level-menu
##################

- Import: See :ref:`The Import menu`
- Export: See :ref:`The Export menu`
- Edit: See :ref:`The Edit menu`
- Exit: This button has no confirmation and will discard everything it has in memory.

The Import menu
###############

Except for the last case, this menu always asks for the source in the next step. The source will always be a single
line of text. Currently if you have more then a single line the CLI may break.

- URL: This may be any URL which is reachable by the requests package. The file then is downloaded and parsed.
- String: This should be a valid one line JSON string which is then parsed by the application.
- File: This is a relative or absolute path to the JSON file. The relative path is relative to your current location,
  not the location of the script.
- Go Back: Go one menu level up again.

The Export menu
###############

Except for the last case, this menu will persist what you have achieved so far with the CLI. In case there is nothing
to be exported you will receive a message for that. Files are overwritten without question, so use the second option
with great care.

- String: Hand back a single line of JSON in the stdout stream.
- File: Write the JSON well formatted to the given location.
- Go Back: Go one menu level up again.

The Edit menu
#############

Except for the last case, this menu will give you the ability to edit your JSON file. Since there is no full Cobbler
instance behind this tool, the logical validations are very loose. However we try to check as much as reasonably
possible.

- Add Operating System Breed: This option is followed by a question for the name. Please only use alphanumeric
  characters, dashes and underscores.
- Remove Operating System Breed: This option is followed by a multiple choice menu where you can select a single Breed.
- Edit the name of an Operating System Breed: This option presents you with a list of Breeds and then gives you an input
  to set the new name.
- Add Operating System Version: If you have a breed then this menu lets you select it and then presents you an input
  where you can choose the name of the Version.
- Remove Operating System Version: If you have a breed, this menu lets you select it and then presents you with a
  menu which does the same for the version.
- Edit the information of an Operating System Version: See :ref:`Remove Operating System Version`
- Start from scratch: Discards everything you have done so far and creates an empty object for you.
- Go Back: Go one menu level up again.

Remove Operating System Version
===============================

- ``signatures``
- ``version_file``
- ``version_file_regex``
- ``kernel_arch``
- ``kernel_arch_regex``
- ``supported_arches``
- ``supported_repo_breeds``
- ``kernel_file``
- ``initrd_file``
- ``isolinux_ok``
- ``default_autoinstall``
- ``kernel_options``
- ``kernel_options_post``
- ``template_files``
- ``boot_files``
- ``boot_loaders``
