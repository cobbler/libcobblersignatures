"""
The CLI. This CLI is interactive and may not be used in scripts. Please use the library for this purpose.
This module contains no logic related to the library, it just contains logic for making it possible to edit the data
managed by it.
"""

import questionary

from libcobblersignatures import Signatures
from libcobblersignatures.enums import ImportTypes, ExportTypes

os_signatures = Signatures()

# questions

main_menu_questions = questionary.select(
    "What do you want to do?", choices=["Import", "Export", "Edit", "Exit"]
)

import_menu_questions = questionary.select(
    "What is your desired source of input?",
    choices=["URL", "String", "File", "Go back"],
)

import_menu_questions2 = questionary.path(
    "Please enter the json in a single line or the source in a single line:"
)


class IntegerValidator(questionary.Validator):
    """
    Validator class which checks if the input is an integer.
    """

    def validate(self, document):
        """
        Validation function which does raise a ValidationError or does not return a value.

        :param document: The user input. Handed over by questionary.
        :raises ValidationError: In case the text could not be parsed to an integer.
        """
        if len(document.text) == 0:
            return
        try:
            int(document.text)
        except ValueError:
            raise questionary.ValidationError(message="Please enter an integer!")


export_menu_questions = [
    {
        "type": "select",
        "name": "export_menu_target",
        "message": "What is your desired export target?",
        "choices": ["String", "File", "Go back"],
    },
    {
        "type": "confirm",
        "name": "export_menu_prettyprint_1",
        "message": "Should the keys be sorted?",
        "when": lambda x: x["export_menu_target"] != "Go back",
    },
    {
        "type": "text",
        "name": "export_menu_prettyprint_2",
        "message": "Which indentation should the keys have? (Hit enter for no indentation or enter a number)",
        #'default': None,
        "validate": IntegerValidator,
        "when": lambda x: x["export_menu_target"] != "Go back",
    },
]

export_menu_questions2 = questionary.text("Please enter the target path")

edit_menu_questions = questionary.select(
    "What do you want to do?",
    choices=[
        "Add Operating System Breed",
        "Remove Operating System Breed",
        "Edit the name of an Operating System Breed",
        "Add Operating System Version",
        "Remove Operating System Version",
        "Edit the information of an Operating System Version",
        "Start from scratch",
        "Go back",
    ],
)

edit_add_os_breed = questionary.text(
    "What should the name of the new Operating System Breed be?"
)

edit_remove_os_breed = [
    {
        "type": "select",
        "name": "edit_remove_os_breed",
        "message": "What Operating System Breed (and all its versions) do you want to remove?",
        "choices": [""],
    }
]

edit_name_os_breed_1 = [
    {
        "type": "select",
        "name": "edit_name_os_breed_1",
        "message": "Which Operating System Breed do you want to edit?",
        "choices": [""],
    }
]

edit_name_os_breed_2 = questionary.text("What shall be the new name?")

edit_add_os_version_1 = [
    {
        "type": "select",
        "name": "edit_add_os_version_1",
        "message": "Under what Operating System Breed shall the new Version be put?",
        "choices": [""],
    }
]

edit_add_os_version_2 = [
    {
        "type": "text",
        "name": "edit_add_os_version_2",
        "message": "What shall be the name of the new version?",
    }
]

edit_remove_os_version_1 = [
    {
        "type": "select",
        "name": "edit_remove_os_version_1",
        "message": "In what Operating System Breed is the to be removed OS Version?",
        "choices": [""],
    }
]

edit_remove_os_version_2 = [
    {
        "type": "select",
        "name": "edit_remove_os_version_2",
        "message": "What is the version that you wish to remove?",
        "choices": [""],
    }
]

edit_information_os_version_which = [
    {
        "type": "select",
        "name": "edit_information_os_version_which",
        "message": "In which operating system breed should the version be?",
        "choices": [""],
    }
]

edit_information_os_version_which_2 = [
    {
        "type": "select",
        "name": "edit_information_os_version_which_2",
        "message": "Which operating system version details do you want to edit?",
        "choices": [""],
    }
]

edit_information_os_version = [
    {
        "type": "select",
        "name": "edit_information_os_version",
        "message": "What key of the Signatures do you want to edit?",
        "choices": [
            "signatures",
            "version_file",
            "version_file_regex",
            "kernel_arch",
            "kernel_arch_regex",
            "supported_arches",
            "supported_repo_breeds",
            "kernel_file",
            "initrd_file",
            "isolinux_ok",
            "default_autoinstall",
            "kernel_options",
            "kernel_options_post",
            "boot_files",
            "Go back",
        ],
    }
]

edit_menu_breed_version_signatures_add = questionary.text(
    "What should the name of the new entry be?"
)

edit_menu_breed_version_signatures_edit = [
    {
        # TODO: Change this to a select since we always know what is in there.
        "type": "text",
        "name": "edit_menu_breed_version_signatures",
        "message": "What signature should be edited?",
    },
    {
        "type": "text",
        "name": "edit_menu_breed_version_signatures_new",
        "message": "What shall be the new name of the selected entry?",
    },
]

edit_menu_breed_version_signatures_delete = questionary.text(
    "What signature should be deleted?"
)

edit_menu_breed_version_version_file = questionary.text(
    'What shall be the new value for the "version_file"?'
)

edit_menu_breed_version_version_file_regex = questionary.text(
    'What shall be the new value for the "version_file_regex"?'
)

edit_menu_breed_version_kernel_arch = questionary.text(
    'What shall be the new value for the "kernel_arch"?'
)

edit_menu_breed_version_kernel_arch_regex = questionary.text(
    'What shall be the new value for the "kernel_arch_regex"?'
)

edit_menu_breed_version_supported_arches_add = questionary.text(
    "What should the name of the new architecture be?"
)

edit_menu_breed_version_supported_arches_edit = [
    {
        # TODO: Change this to a select since we always know what is in there.
        "type": "text",
        "name": "edit_menu_breed_version_supported_arches_edit",
        "message": "What supported architecture shall be edited?",
    },
    {
        "type": "text",
        "name": "edit_menu_breed_version_supported_arches_edit_new",
        "message": "What shall be the new name of the selected architecture?",
    },
]

edit_menu_breed_version_supported_arches_delete = questionary.text(
    "What architecture shall be deleted from the operating system version?"
)

edit_menu_breed_version_supported_repo_breeds_add = questionary.text(
    "What should the name of the new repository breed be?"
)

edit_menu_breed_version_supported_repo_breeds_edit = [
    {
        # TODO: Change this to a select since we always know what is in there.
        "type": "text",
        "name": "edit_menu_breed_version_supported_repo_breeds_edit",
        "message": "What repository breed shall be edited?",
    },
    {
        "type": "text",
        "name": "edit_menu_breed_version_supported_repo_breeds_edit_new",
        "message": "What shall be the new name of the selected repository breed?",
    },
]

edit_menu_breed_version_supported_repo_breeds_delete = questionary.text(
    "What repository breed shall be deleted from the operating system version?"
)

edit_menu_breed_version_kernel_file = questionary.text(
    'What should the new value of the "kernel_file" be?'
)

edit_menu_breed_version_initrd_file = questionary.text(
    'What should the new value of the "initrd_file" be?'
)

edit_menu_breed_version_isolinux_ok = questionary.confirm(
    "Whether to set this to true (y) or not (N)?", default=False
)

edit_menu_breed_version_default_autoinstall = questionary.text(
    'What should the new value of the "default_autoinstall" be?'
)

edit_menu_breed_version_kernel_options = questionary.text(
    'What should the new value of the "kernel_options" be?'
)

edit_menu_breed_version_kernel_options_post = questionary.text(
    'What should the new value of the "kernel_options_post" be?'
)

edit_menu_breed_version_boot_files_add = questionary.text(
    "What should the name of the new boot files entry be?"
)

edit_menu_breed_version_boot_files_edit = [
    {
        # TODO: Change this to a select since we always know what is in there.
        "type": "text",
        "name": "edit_menu_breed_version_boot_files_edit",
        "message": "What boot files entry shall be edited?",
    },
    {
        "type": "text",
        "name": "edit_menu_breed_version_boot_files_edit_new",
        "message": "What shall be the new name of the selected file entry?",
    },
]

edit_menu_breed_version_boot_files_delete = questionary.text(
    "What boot files entry shall be deleted from the operating system version?"
)

edit_menu_version_add_remove_edit = questionary.select(
    "What do you want to do?", choices=["Add", "Edit", "Remove"]
)


# definitions


def get_os_breed_names() -> list:
    """
    This searches for all names of the operation system breeds in the current instance of the library.

    :return: An empty list if no names are found. Otherwise all names of the operating system breeds.
    """
    if os_signatures is None:
        raise TypeError("os_signatures object must not be none!")
    names = []
    for v in os_signatures.osbreeds:
        names.append(v.name)
    return names


def get_os_version_names(breed) -> list:
    """
    This searches for all names of the given breed in the current instance of the library.

    :param breed: This is the breed object.
    :return: The list of all names if the breed has them. Otherwise an empty list.
    """
    if os_signatures is None:
        raise TypeError("os_signatures object must not be none!")
    index = os_signatures.get_breed_index_by_name(breed)
    if index >= 0:
        return list(os_signatures.osbreeds[index].osversions.keys())
    else:
        print("Operating System Breed not found. Doing nothing.")
        return []


def update_choices(question: list, values: list):
    """
    Update the choices of the first question to the attached list and add a "Go Back" option.

    :param question: The list with the dictionaries with the questions.
    :param values: The values which will replace the old choices.
    """
    if len(values) == 0:
        values = []
    values.append("Go Back")

    if not isinstance(question[0], dict):
        raise TypeError("First element of list question must be of type dict!")
    question[0].update({"choices": values})


def prepare_version_edit_information_os_version(version):
    """
    Add the information of an :class:`Osversion` to the CLI prompt in the edit menu.

    :param version: The :class:`Osversion` to fetch information of.
    """
    values = [
        'signatures - "%s"' % str(version.signatures),
        'version_file - "%s"' % version.version_file,
        'version_file_regex - "%s"' % version.version_file_regex,
        'kernel_arch - "%s"' % version.kernel_arch,
        'kernel_arch_regex - "%s"' % version.kernel_arch_regex,
        'supported_arches - "%s"' % str(version.supported_arches),
        'supported_repo_breeds - "%s"' % str(version.supported_repo_breeds),
        'kernel_file - "%s"' % version.kernel_file,
        'initrd_file - "%s"' % version.initrd_file,
        'isolinux_ok - "%s"' % version.isolinux_ok,
        'default_autoinstall - "%s"' % version.default_autoinstall,
        'kernel_options - "%s"' % version.kernel_options,
        'kernel_options_post - "%s"' % version.kernel_options_post,
        'boot_files - "%s"' % str(version.boot_files),
    ]
    update_choices(edit_information_os_version, values)


def reset_edit_information_os_version():
    """
    Reset the CLI edit prompt of the :class:`Osversion`.
    """
    values = [
        "signatures",
        "version_file",
        "version_file_regex",
        "kernel_arch",
        "kernel_arch_regex",
        "supported_arches",
        "supported_repo_breeds",
        "kernel_file",
        "initrd_file",
        "isolinux_ok",
        "default_autoinstall",
        "kernel_options",
        "kernel_options_post",
        "boot_files",
    ]
    update_choices(edit_information_os_version, values)


def import_menu():
    """
    Second level menu with the purpose to catch all functionality related to importing the data from a source.
    """
    choice_import_menu = import_menu_questions.ask()
    if choice_import_menu in ["URL", "File", "String"]:
        result_import_menu_2 = import_menu_questions2.ask()
        if choice_import_menu == "URL":
            import_type = ImportTypes.URL
        elif choice_import_menu == "File":
            import_type = ImportTypes.FILE
        elif choice_import_menu == "String":
            import_type = ImportTypes.STRING
        else:
            return
        input_import_source = result_import_menu_2
        if input_import_source == "":
            print("Source was not entered correctly.")
            return
        os_signatures.importsignatures(import_type, input_import_source)
        os_signatures.jsontomodels()
    else:
        print("Unknown import option selected. Returning to main menu.")


def export_menu():
    """
    Second level menu with the purpose to catch all functionality related to exporting the data to a target.
    """
    export_menu_answers = questionary.prompt(export_menu_questions)
    choice_export_menu = export_menu_answers.get("export_menu_target")
    choice_pretty_print_sort = export_menu_answers.get("export_menu_prettyprint_1")
    choice_pretty_print_indent = export_menu_answers.get("export_menu_prettyprint_2")
    if not choice_pretty_print_indent:
        choice_pretty_print_indent = None
    else:
        choice_pretty_print_indent = int(choice_pretty_print_indent)

    if choice_export_menu == "String":
        print(
            os_signatures.exportsignatures(
                ExportTypes.STRING,
                sort_keys=choice_pretty_print_sort,
                indent=choice_pretty_print_indent,
            )
        )
    elif choice_export_menu == "File":
        input_export_menu_2 = export_menu_questions2.ask()
        if input_export_menu_2 == "":
            print(
                "Target path for the file was not entered correctly. Returning to main menu."
            )
            return
        os_signatures.exportsignatures(
            ExportTypes.FILE,
            input_export_menu_2,
            choice_pretty_print_sort,
            choice_pretty_print_indent,
        )
    elif choice_export_menu == "Go back":
        return
    else:
        print("Unknown option selected. Returning to the main menu.")
        return


def edit_menu():
    """
    Second level menu with the purpose to catch all functionality related to editing the current loaded information.
    """
    global os_signatures
    choice_edit_menu = edit_menu_questions.ask()
    if choice_edit_menu == "Add Operating System Breed":
        result_edit_add_os_breed = edit_add_os_breed.ask()
        if not result_edit_add_os_breed:
            print("Empty Operating System Breed name is not allowed. Skipping add.")
            return
        if result_edit_add_os_breed in [
            version.name for version in os_signatures.osbreeds
        ]:
            print(
                'Chosen name "%s" already in the list of Operating System Breeds.'
                % result_edit_add_os_breed
            )
            return
        os_signatures.addosbreed(result_edit_add_os_breed)
        print(
            "We now have %s Operating System Breeds in this file."
            % len(os_signatures.osbreeds)
        )
    elif choice_edit_menu == "Remove Operating System Breed":
        update_choices(edit_remove_os_breed, get_os_breed_names())
        result_edit_remove_os_breed = questionary.prompt(edit_remove_os_breed)
        name_to_find = result_edit_remove_os_breed["edit_remove_os_breed"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if (
            index != -1
            and result_edit_remove_os_breed == os_signatures.osbreeds[index].name
        ):
            os_signatures.removeosbreed(index)
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Edit the name of an Operating System Breed":
        update_choices(edit_name_os_breed_1, get_os_breed_names())
        result_edit_name_os_breed_1 = questionary.prompt(edit_name_os_breed_1)
        name_to_find = result_edit_name_os_breed_1["edit_name_os_breed_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            result_edit_name_os_breed_2 = edit_name_os_breed_2.ask()
            os_signatures.osbreeds[index].name = result_edit_name_os_breed_2
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Add Operating System Version":
        update_choices(edit_add_os_version_1, get_os_breed_names())
        result_edit_add_os_version_1 = questionary.prompt(edit_add_os_version_1)
        name_to_find = result_edit_add_os_version_1["edit_add_os_version_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            result_edit_add_os_version_2 = questionary.prompt(edit_add_os_version_2)
            name_to_find_1 = result_edit_add_os_version_2["edit_add_os_version_2"]
            os_signatures.addosversion(index, name_to_find_1, None)
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Remove Operating System Version":
        update_choices(edit_remove_os_version_1, get_os_breed_names())
        result_edit_remove_os_version_1 = questionary.prompt(edit_remove_os_version_1)
        name_to_find = result_edit_remove_os_version_1["edit_remove_os_version_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            update_choices(edit_remove_os_version_2, get_os_version_names(name_to_find))
            result_edit_remove_os_version_2 = questionary.prompt(
                edit_remove_os_version_2
            )
            name_to_find_1 = result_edit_remove_os_version_2["edit_remove_os_version_2"]
            os_signatures.removeosversion(index, name_to_find_1)
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Edit the information of an Operating System Version":
        edit_menu_breed_version_info()
    elif choice_edit_menu == "Start from scratch":
        os_signatures = Signatures()
    elif choice_edit_menu == "Go Back":
        return
    else:
        print("Unknown option selected. Returning to the main menu.")


def edit_menu_breed_version_info_signatures(my_osversion):
    """
    Fourth level menu to edit the ``signatures`` of an :class:`Osversion`.

    :param my_osversion: The Osversion to edit.
    """
    result_signatures_choice = edit_menu_version_add_remove_edit.ask()
    if result_signatures_choice == "Add":
        new_value_signature = edit_menu_breed_version_signatures_add.ask()
        my_osversion.signatures.add(new_value_signature)
    elif result_signatures_choice == "Edit":
        new_value_edit_signatures = questionary.prompt(
            edit_menu_breed_version_signatures_edit
        )
        try:
            my_osversion.signatures.remove(
                new_value_edit_signatures["edit_menu_breed_version_signatures"]
            )
        except KeyError:
            print("Chosen key not found. Aborting value edit of signatures!")
            return
        my_osversion.signatures.add(
            new_value_edit_signatures["edit_menu_breed_version_signatures_new"]
        )
    elif result_signatures_choice == "Remove":
        value_to_be_removed = edit_menu_breed_version_signatures_delete.ask()
        my_osversion.signatures.remove(value_to_be_removed)
    else:
        print("Unknown option selected.")


def edit_menu_breed_version_info_supported_arches(my_osversion):
    result_supported_arches_choice = edit_menu_version_add_remove_edit.ask()
    if result_supported_arches_choice == "Add":
        new_value_supported_arches = edit_menu_breed_version_supported_arches_add.ask()
        my_osversion.supported_arches.add(new_value_supported_arches)
    elif result_supported_arches_choice == "Edit":
        new_value_edit_arches = questionary.prompt(
            edit_menu_breed_version_supported_arches_edit
        )
        try:
            my_osversion.supported_arches.remove(
                new_value_edit_arches["edit_menu_breed_version_supported_arches_edit"]
            )
        except KeyError:
            print("Chosen key not found. Aborting value edit of supported_arches!")
            return
        my_osversion.supported_arches.add(
            new_value_edit_arches["edit_menu_breed_version_supported_arches_edit_new"]
        )
    elif result_supported_arches_choice == "Remove":
        value_to_be_removed = edit_menu_breed_version_supported_arches_delete.ask()
        my_osversion.supported_arches.remove(value_to_be_removed)
    else:
        print("Unknown option selected.")
    # TODO: Validation of arches (only with warning)


def edit_menu_breed_version_info_supported_repo_breeds(my_osversion):
    result_repo_breeds_choice = edit_menu_version_add_remove_edit.ask()
    if result_repo_breeds_choice == "Add":
        new_value_supported_repo_breed = (
            edit_menu_breed_version_supported_repo_breeds_add.ask()
        )
        my_osversion.supported_repo_breeds.add(new_value_supported_repo_breed)
    elif result_repo_breeds_choice == "Edit":
        new_value_edit_supported_repo_breeds = questionary.prompt(
            edit_menu_breed_version_supported_repo_breeds_edit
        )
        try:
            my_osversion.supported_repo_breeds.remove(
                new_value_edit_supported_repo_breeds[
                    "edit_menu_breed_version_supported_repo_breeds_edit"
                ]
            )
        except KeyError:
            print("Chosen key not found. Aborting value edit of supported_repo_breeds!")
            return
        my_osversion.supported_repo_breeds.add(
            new_value_edit_supported_repo_breeds[
                "edit_menu_breed_version_supported_repo_breeds_edit_new"
            ]
        )
    elif result_repo_breeds_choice == "Remove":
        value_to_be_removed = edit_menu_breed_version_supported_repo_breeds_delete.ask()
        my_osversion.supported_repo_breeds.remove(value_to_be_removed)
    else:
        print("Unknown option selected.")
    # TODO: Validation for choices (only with warning)


def edit_menu_breed_version_info_boot_files(my_osversion):
    result_boot_files_choice = edit_menu_version_add_remove_edit.ask()
    if result_boot_files_choice == "Add":
        new_value_boot_files_add = edit_menu_breed_version_boot_files_add.ask()
        my_osversion.boot_files.add(new_value_boot_files_add)
    elif result_boot_files_choice == "Edit":
        new_value_edit_boot_files = questionary.prompt(
            edit_menu_breed_version_boot_files_edit
        )
        try:
            my_osversion.boot_files.remove(
                new_value_edit_boot_files["edit_menu_breed_version_boot_files_edit"]
            )
        except KeyError:
            print("Chosen key not found. Aborting value edit of boot_files!")
            return
        my_osversion.boot_files.add(
            new_value_edit_boot_files["edit_menu_breed_version_boot_files_edit_new"]
        )
    elif result_boot_files_choice == "Remove":
        value_to_be_removed = edit_menu_breed_version_boot_files_delete.ask()
        my_osversion.boot_files.remove(value_to_be_removed)
    else:
        print("Unknown option selected.")


def edit_menu_breed_version_info():
    """
    Third level menu to edit the information of an :class:`Osversion`.
    """
    # Prechoose which OsBreed and OsVersion should be manipulated
    update_choices(edit_information_os_version_which, get_os_breed_names())
    choice_edit_information_os_version_which = questionary.prompt(
        edit_information_os_version_which
    )
    breed_index_name = choice_edit_information_os_version_which[
        "edit_information_os_version_which"
    ]
    if breed_index_name == "Go Back":
        return
    elif breed_index_name == "":
        print("Unknown option selected. Returning to main menu.")
        return
    update_choices(
        edit_information_os_version_which_2, get_os_version_names(breed_index_name)
    )
    choice_edit_information_os_version_which_2 = questionary.prompt(
        edit_information_os_version_which_2
    )
    my_os_version_name = choice_edit_information_os_version_which_2[
        "edit_information_os_version_which_2"
    ]
    if my_os_version_name == "Go Back":
        return
    elif my_os_version_name == "":
        print("Unknown option selected. Returning to main menu.")
        return

    # Presave index for OsBreed
    breed_index = os_signatures.get_breed_index_by_name(breed_index_name)
    my_osversion = os_signatures.osbreeds[breed_index].osversions.get(
        my_os_version_name
    )

    # Prepare the values for the attribute editing
    prepare_version_edit_information_os_version(my_osversion)

    # Do the actual editing
    edit_information_os_version_result = questionary.prompt(edit_information_os_version)
    choice_edit_information_os_version = edit_information_os_version_result[
        "edit_information_os_version"
    ]
    print(choice_edit_information_os_version)
    if choice_edit_information_os_version.startswith("signatures"):
        edit_menu_breed_version_info_signatures(my_osversion)
    elif choice_edit_information_os_version.startswith("version_file"):
        new_value_version_file = edit_menu_breed_version_version_file.ask()
        my_osversion.version_file = new_value_version_file
    elif choice_edit_information_os_version.startswith("version_file_regex"):
        new_value_version_file_regex = edit_menu_breed_version_version_file_regex.ask()
        my_osversion.version_file_regex = new_value_version_file_regex
    elif choice_edit_information_os_version.startswith("kernel_arch"):
        new_value_kernel_arch = edit_menu_breed_version_kernel_arch.ask()
        my_osversion.kernel_arch = new_value_kernel_arch
    elif choice_edit_information_os_version.startswith("kernel_arch_regex"):
        new_value_kernel_arch_regex = edit_menu_breed_version_kernel_arch_regex.ask()
        my_osversion.kernel_arch_regex = new_value_kernel_arch_regex
    elif choice_edit_information_os_version.startswith("supported_arches"):
        edit_menu_breed_version_info_supported_arches(my_osversion)
    elif choice_edit_information_os_version.startswith("supported_repo_breeds"):
        edit_menu_breed_version_info_supported_repo_breeds(my_osversion)
    elif choice_edit_information_os_version.startswith("kernel_file"):
        new_value_kernel_file = edit_menu_breed_version_kernel_file.ask()
        my_osversion.kernel_file = new_value_kernel_file
    elif choice_edit_information_os_version.startswith("initrd_file"):
        new_value_initrd_file = edit_menu_breed_version_initrd_file.ask()
        my_osversion.kernel_file = new_value_initrd_file
    elif choice_edit_information_os_version.startswith("isolinux_ok"):
        new_value_isolinux_ok = edit_menu_breed_version_isolinux_ok.ask()
        my_osversion.isolinux_ok = new_value_isolinux_ok
    elif choice_edit_information_os_version.startswith("default_autoinstall"):
        # TODO: Filename validation
        new_value_default_autoinstall = (
            edit_menu_breed_version_default_autoinstall.ask()
        )
        my_osversion.default_autoinstall = new_value_default_autoinstall
    elif choice_edit_information_os_version.startswith("kernel_options"):
        new_value_kernel_options = edit_menu_breed_version_kernel_options.ask()
        my_osversion.kernel_options = new_value_kernel_options
    elif choice_edit_information_os_version.startswith("kernel_options_post"):
        new_value_kernel_options_post = (
            edit_menu_breed_version_kernel_options_post.ask()
        )
        my_osversion.kernel_options_post = new_value_kernel_options_post
    elif choice_edit_information_os_version.startswith("boot_files"):
        edit_menu_breed_version_info_boot_files(my_osversion)
    else:
        return
    reset_edit_information_os_version()


def main():
    """
    The main entrypoint for the CLI. This is called when you execute the CLI. The exitcode of the application is zero.
    This is a first level menu.
    """
    main_menu_option_selected = 0
    while main_menu_option_selected != 3:
        chosen_option = main_menu_questions.ask()
        if chosen_option == "Import":
            main_menu_option_selected = 0
            import_menu()
        elif chosen_option == "Export":
            main_menu_option_selected = 1
            export_menu()
        elif chosen_option == "Edit":
            main_menu_option_selected = 2
            edit_menu()
        elif chosen_option == "Exit":
            main_menu_option_selected = 3
            print("Any progress which is not exported will be lost. Bye.")
        else:
            main_menu_option_selected = -1
            print("Unknown option chosen. Redisplaying menu.")
    exit(0)


if __name__ == "__main__":
    main()
