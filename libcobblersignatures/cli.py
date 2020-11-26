"""
The CLI. This CLI is interactive and may not be used in scripts. Please use the library for this purpose.

This module contains no logic related to the library it just contains logic for making it possible to edit the data
managed by it.
"""
from PyInquirer import prompt

from libcobblersignatures.signatures import Signatures, ImportTypes, ExportTypes

os_signatures = Signatures()

main_menu_questions = [
    {
        "type": "list",
        "name": "main_menu",
        "message": "What do you want to do?",
        "choices": [
            "Import",
            "Export",
            "Edit",
            "Exit"
        ]
    }
]

import_menu_questions = [
    {
        "type": "list",
        "name": "import_menu_source",
        "message": "What is your desired source of input?",
        "choices": [
            "URL",
            "String",
            "File",
            "Go Back"
        ]
    }
]

import_menu_questions2 = [
    {
        "type": "input",
        "name": "import_menu_signatures",
        "message": "Please enter the json in a single line or the source in a single line:",
    }
]

export_menu_questions = [
    {
        "type": "list",
        "name": "export_menu_sources",
        "message": "What is your desired export target?",
        "choices": [
            "String",
            "File",
            "Go Back"
        ]
    }
]

export_menu_questions2 = [
    {
        "type": "input",
        "name": "export_menu_signatures",
        "message": "Please enter the target path",
    }
]

edit_menu_questions = [
    {
        "type": "list",
        "name": "edit_main_menu",
        "message": "What do you want to do?",
        "choices": [
            "Add Operating System Breed",
            "Remove Operating System Breed",
            "Edit the name of an Operating System Breed",
            "Add Operating System Version",
            "Remove Operating System Version",
            "Edit the information of an Operating System Version",
            "Start from scratch",
            "Go Back"
        ]
    }
]

edit_add_os_breed = [
    {
        "type": "input",
        "name": "edit_add_os_breed",
        "message": "What should the name of the new Operating System Breed be?",
    }
]

edit_remove_os_breed = [
    {
        "type": "list",
        "name": "edit_remove_os_breed",
        "message": "What Operating System Breed (and all its versions) do you want to remove?",
        "choices": [],
    }
]

edit_name_os_breed_1 = [
    {
        "type": "list",
        "name": "edit_name_os_breed_1",
        "message": "Which Operating System Breed do you want to edit?",
        "choice": [],
    }
]

edit_name_os_breed_2 = [
    {
        "type": "input",
        "name": "edit_name_os_breed_2",
        "message": "What shall be the new name?",
    }
]

edit_add_os_version_1 = [
    {
        "type": "list",
        "name": "edit_add_os_version_1",
        "message": "Under what Operating System Breed shall the new Version be put?",
        "choice": []
    }
]

edit_add_os_version_2 = [
    {
        "type": "input",
        "name": "edit_add_os_version_2",
        "message": "What shall be the name of the new version?",
    }
]

edit_remove_os_version_1 = [
    {
        "type": "list",
        "name": "edit_remove_os_version_1",
        "message": "In what Operating System Breed is the to be removed OS Version?",
        "choices": [],
    }
]

edit_remove_os_version_2 = [
    {
        "type": "list",
        "name": "edit_remove_os_version_2",
        "message": "What is the version that you wish to remove?",
        "choices": [],
    }
]

edit_information_os_version_which = [
    {
        "type": "list",
        "name": "edit_information_os_version_which",
        "message": "In which operating system breed should the version be?",
        "choices": []
    }
]

edit_information_os_version_which_2 = [
    {
        "type": "list",
        "name": "edit_information_os_version_which_2",
        "message": "Which operating system version details do you want to edit?",
        "choices": []
    }
]

edit_information_os_version = [
    {
        "type": "list",
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
            "Go Back"
        ]
    }
]

edit_menu_breed_version_signatures_add = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_signatures_add",
        "message": "What should the name of the new entry be?"
    }
]

edit_menu_breed_version_signatures_edit = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_signatures",
        "message": "What signature should be edited?",
        "choices": []
    }, {
        "type": "input",
        "name": "edit_menu_breed_version_signatures_new",
        "message": "What shall be the new name of the selected entry?"
    }
]

edit_menu_breed_version_signatures_delete = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_signatures",
        "message": "What signature should be deleted?",
        "choices": []
    }
]

edit_menu_breed_version_version_file = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_version_file",
        "message": "What shall be the new value for the \"version_file\"?"
    }
]

edit_menu_breed_version_version_file_regex = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_version_file_regex",
        "message": "What shall be the new value for the \"version_file_regex\"?"
    }
]

edit_menu_breed_version_kernel_arch = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_kernel_arch",
        "message": "What shall be the new value for the \"kernel_arch\"?"
    }
]

edit_menu_breed_version_kernel_arch_regex = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_kernel_arch_regex",
        "message": "What shall be the new value for the \"kernel_arch_regex\"?"
    }
]

edit_menu_breed_version_supported_arches_add = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_supported_arches_add",
        "message": "What should the name of the new architecture be?"
    }
]

edit_menu_breed_version_supported_arches_edit = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_supported_arches_edit",
        "message": "What supported architecture shall be edited?",
        "choices": []
    }, {
        "type": "input",
        "name": "edit_menu_breed_version_supported_arches_edit_new",
        "message": "What shall be the new name of the selected architecture?"
    }
]

edit_menu_breed_version_supported_arches_delete = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_supported_arches_delete",
        "message": "What architecture shall be deleted from the operating system version?",
        "choices": []
    }
]

edit_menu_breed_version_supported_repo_breeds_add = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_supported_repo_breeds_add",
        "message": "What should the name of the new repository breed be?"
    }
]
edit_menu_breed_version_supported_repo_breeds_edit = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_supported_repo_breeds_edit",
        "message": "What repository breed shall be edited?",
        "choices": []
    }, {
        "type": "input",
        "name": "edit_menu_breed_version_supported_repo_breeds_edit_new",
        "message": "What shall be the new name of the selected repository breed?"
    }
]

edit_menu_breed_version_supported_repo_breeds_delete = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_supported_repo_breeds_delete",
        "message": "What repository breed shall be deleted from the operating system version?",
        "choices": []
    }
]

edit_menu_breed_version_kernel_file = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_kernel_file",
        "message": "What should the new value of the \"kernel_file\" be?"
    }
]

edit_menu_breed_version_initrd_file = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_initrd_file",
        "message": "What should the new value of the \"initrd_file\" be?"
    }
]

edit_menu_breed_version_isolinux_ok = [
    {
        "type": "confirm",
        "name": "edit_menu_breed_version_isolinux_ok",
        "message": "Whether to set this to true (y) or not (N)?"
    }
]

edit_menu_breed_version_default_autoinstall = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_default_autoinstall",
        "message": "What should the new value of the \"default_autoinstall\" be?"
    }
]

edit_menu_breed_version_kernel_options = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_kernel_options",
        "message": "What should the new value of the \"kernel_options\" be?"
    }
]

edit_menu_breed_version_kernel_options_post = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_kernel_options_post",
        "message": "What should the new value of the \"kernel_options_post\" be?"
    }
]

edit_menu_breed_version_boot_files_add = [
    {
        "type": "input",
        "name": "edit_menu_breed_version_boot_files_add",
        "message": "What should the name of the new boot files entry be?"
    }
]

edit_menu_breed_version_boot_files_edit = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_boot_files_edit",
        "message": "What boot files entry shall be edited?",
        "choices": []
    }, {
        "type": "input",
        "name": "edit_menu_breed_version_boot_files_edit_new",
        "message": "What shall be the new name of the selected file entry?"
    }
]

edit_menu_breed_version_boot_files_delete = [
    {
        "type": "list",
        "name": "edit_menu_breed_version_boot_files_delete",
        "message": "What boot files entry shall be deleted from the operating system version?",
        "choices": []
    }
]

edit_menu_version_add_remove_edit = [
    {
        "type": "list",
        "name": "edit_menu_version_add_remove_edit",
        "message": "What do you want to do?",
        "choices": [
            "Add",
            "Edit",
            "Remove"
        ]
    }
]


def get_os_breed_names():
    """
    This searches for all names of the operation system breeds in the current instance of the library.

    :return: An empty list if no names are found. Otherwise all names of the operating system breeds.
    :rtype: list
    """
    names = []
    for v in os_signatures.osbreeds:
        names.append(v.name)
    return names


def get_os_version_names(breed):
    """
    This searches for all names of the given breed in the current instance of the library.

    :param breed: This is the breed object.
    :return: The list of all names if the breed has them. Otherwise an empty list.
    :rtype: list
    """
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
    question[0].update({"choices": values})


def prepare_version_edit_information_os_version(version):
    """
    Add the information of an :class:`Osversion` to the CLI prompt in the edit menu.

    :param version: The :class:`Osversion` to fetch information of.
    """
    values = [
        "signatures - %s" % str(version.signatures),
        "version_file - %s" % version.version_file,
        "version_file_regex - %s" % version.version_file_regex,
        "kernel_arch - %s" % version.kernel_arch,
        "kernel_arch_regex - %s" % version.kernel_arch_regex,
        "supported_arches - %s" % str(version.supported_arches),
        "supported_repo_breeds - %s" % str(version.supported_repo_breeds),
        "kernel_file - %s" % version.kernel_file,
        "initrd_file - %s" % version.initrd_file,
        "isolinux_ok - %s" % version.isolinux_ok,
        "default_autoinstall - %s" % version.default_autoinstall,
        "kernel_options - %s" % version.kernel_options,
        "kernel_options_post - %s" % version.kernel_options_post,
        "boot_files - %s" % str(version.boot_files)
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
        "boot_files"
    ]
    update_choices(edit_information_os_version, values)


def import_menu():
    """
    Second level menu with the purpose to catch all functionality related to importing the data from a source.
    """
    result_import_menu = prompt(import_menu_questions)
    choice_import_menu = result_import_menu.get("import_menu_source", "")
    if choice_import_menu in ["URL", "File", "String"]:
        result_import_menu_2 = prompt(import_menu_questions2)
        if choice_import_menu == "URL":
            import_type = ImportTypes.URL
        elif choice_import_menu == "File":
            import_type = ImportTypes.FILE
        elif choice_import_menu == "String":
            import_type = ImportTypes.STRING
        else:
            return
        input_import_source = result_import_menu_2.get("import_menu_signatures", "")
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
    result_export_menu = prompt(export_menu_questions)
    choice_export_menu = result_export_menu.get("export_menu_sources", "")
    if choice_export_menu == "String":
        os_signatures.modelstojson()
        print(os_signatures.exportsignatures(ExportTypes.STRING))
    elif choice_export_menu == "File":
        result_export_menu_2 = prompt(export_menu_questions2)
        input_export_menu_2 = result_export_menu_2.get("export_menu_signatures", "")
        if input_export_menu_2 == "":
            print("Targetpath for the file was not correctly entered. Returning to main menu.")
            return
        os_signatures.modelstojson()
        os_signatures.exportsignatures(ExportTypes.FILE, input_export_menu_2)
    else:
        print("Unknown option selected. Returning to the main menu.")
        return


def edit_menu():
    """
    Second level menu with the purpose to catch all functionality related to editing the current loaded information.
    """
    global os_signatures
    result_edit_menu = prompt(edit_menu_questions)
    choice_edit_menu = result_edit_menu.get("edit_main_menu", "")
    if choice_edit_menu == "Add Operating System Breed":
        result_edit_add_os_breed = prompt(edit_add_os_breed)
        os_signatures.addosbreed(result_edit_add_os_breed["edit_add_os_breed"])
        print("We now have %s Operating System Breeds in this file." % len(os_signatures.osbreeds))
    elif choice_edit_menu == "Remove Operating System Breed":
        update_choices(edit_remove_os_breed, get_os_breed_names())
        result_edit_remove_os_breed = prompt(edit_remove_os_breed)
        name_to_find = result_edit_remove_os_breed["edit_remove_os_breed"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and result_edit_remove_os_breed["edit_remove_os_breed"] == os_signatures.osbreeds[index].name:
            os_signatures.removeosbreed(index)
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Edit the name of an Operating System Breed":
        update_choices(edit_name_os_breed_1, get_os_breed_names())
        result_edit_name_os_breed_1 = prompt(edit_name_os_breed_1)
        name_to_find = result_edit_name_os_breed_1["edit_name_os_breed_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            result_edit_name_os_breed_2 = prompt(edit_name_os_breed_2)
            os_signatures.osbreeds[index].name = result_edit_name_os_breed_2["edit_name_os_breed_2"]
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Add Operating System Version":
        update_choices(edit_add_os_version_1, get_os_breed_names())
        result_edit_add_os_version_1 = prompt(edit_add_os_version_1)
        name_to_find = result_edit_add_os_version_1["edit_add_os_version_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            result_edit_add_os_version_2 = prompt(edit_add_os_version_2)
            os_signatures.addosversion(index, result_edit_add_os_version_2["edit_add_os_version_2"], None)
        else:
            print("Operating System Breed not found. Doing nothing.")
    elif choice_edit_menu == "Remove Operating System Version":
        update_choices(edit_remove_os_version_1, get_os_breed_names())
        result_edit_remove_os_version_1 = prompt(edit_remove_os_version_1)
        name_to_find = result_edit_remove_os_version_1["edit_remove_os_version_1"]
        index = os_signatures.get_breed_index_by_name(name_to_find)
        if index != -1 and name_to_find == os_signatures.osbreeds[index].name:
            result_edit_remove_os_version_2 = prompt(edit_remove_os_version_2)
            os_signatures.removeosversion(index, result_edit_remove_os_version_2["edit_remove_os_version_2"])
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


def edit_menu_breed_version_info():
    """
    Third level menu to edit the information of an :class:`Osversion`.
    """
    # Prechoose which OsBreed and OsVersion should be manipulated
    update_choices(edit_information_os_version_which, get_os_breed_names())
    edit_information_os_version_which_result = prompt(edit_information_os_version_which)
    choice_edit_information_os_version_which = edit_information_os_version_which_result \
        .get("edit_information_os_version_which", "")
    if choice_edit_information_os_version_which == "Go Back":
        return
    elif choice_edit_information_os_version_which == "":
        print("Unknown option selected. Returning to main menu.")
        return
    update_choices(edit_information_os_version_which_2,
                   get_os_version_names(choice_edit_information_os_version_which))
    edit_information_os_version_which_result_2 = prompt(edit_information_os_version_which_2)
    choice_edit_information_os_version_which_2 = \
        edit_information_os_version_which_result_2.get("edit_information_os_version_which_2", "")
    if choice_edit_information_os_version_which_2 == "Go Back":
        return
    elif choice_edit_information_os_version_which_2 == "":
        print("Unknown option selected. Returning to main menu.")
        return

    # Presave index for OsBreed
    breed_index = os_signatures.get_breed_index_by_name(choice_edit_information_os_version_which)

    # Prepare the values for the attribute editing
    prepare_version_edit_information_os_version(
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2)
    )

    # Do the actual editing
    result_edit_information_os_version = prompt(edit_information_os_version)
    choice_edit_information_os_version = result_edit_information_os_version.get("edit_information_os_version", "")
    if choice_edit_information_os_version == "signatures":
        result_signatures_choice = prompt(edit_menu_version_add_remove_edit)
        if result_signatures_choice["edit_menu_version_add_remove_edit"] == "Add":
            new_value_signature = prompt(edit_menu_breed_version_signatures_add)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .signatures.append(new_value_signature["edit_menu_breed_version_signatures_add"])
        elif result_signatures_choice["edit_menu_version_add_remove_edit"] == "Edit":
            new_value_edit_signatures = prompt(edit_menu_breed_version_signatures_edit)
            index_to_change = os_signatures.osbreeds[breed_index].osversions \
                .get(choice_edit_information_os_version_which_2) \
                .signatures.index(new_value_edit_signatures["edit_menu_breed_version_signatures"])
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .signatures[index_to_change] = new_value_edit_signatures["edit_menu_breed_version_signatures_new"]
        elif result_signatures_choice["edit_menu_version_add_remove_edit"] == "Remove":
            value_to_be_removed = prompt(edit_menu_breed_version_signatures_delete)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .signatures.remove(value_to_be_removed["edit_menu_breed_version_signatures"])
        else:
            print("Unknown option selected.")
    elif choice_edit_information_os_version == "version_file":
        new_value_version_file = prompt(edit_menu_breed_version_version_file)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).version_file \
            = new_value_version_file["edit_menu_breed_version_version_file"]
    elif choice_edit_information_os_version == "version_file_regex":
        new_value_version_file_regex = prompt(edit_menu_breed_version_version_file_regex)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
            .version_file_regex = new_value_version_file_regex["edit_menu_breed_version_version_file_regex"]
    elif choice_edit_information_os_version == "kernel_arch":
        new_value_kernel_arch = prompt(edit_menu_breed_version_kernel_arch)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).kernel_arch \
            = new_value_kernel_arch["edit_menu_breed_version_kernel_arch"]
    elif choice_edit_information_os_version == "kernel_arch_regex":
        new_value_kernel_arch_regex = prompt(edit_menu_breed_version_kernel_arch_regex)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
            .kernel_arch_regex = new_value_kernel_arch_regex["edit_menu_breed_version_kernel_arch_regex"]
    elif choice_edit_information_os_version == "supported_arches":
        result_supported_arches_choice = prompt(edit_menu_version_add_remove_edit)
        choice_result_supported_arches_choice = result_supported_arches_choice \
            .get("edit_menu_version_add_remove_edit", "")
        if choice_result_supported_arches_choice == "Add":
            new_value_supported_arches = prompt(edit_menu_breed_version_supported_arches_add)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_arches.append(new_value_supported_arches["edit_menu_breed_version_supported_arches_add"])
        elif choice_result_supported_arches_choice == "Edit":
            new_value_edit_arches = prompt(edit_menu_breed_version_supported_arches_edit)
            index_to_change = os_signatures.osbreeds[breed_index].osversions \
                .get(choice_edit_information_os_version_which_2) \
                .supported_arches.index(new_value_edit_arches["edit_menu_breed_version_supported_arches_edit"])
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_arches[index_to_change] = new_value_edit_arches[
                "edit_menu_breed_version_supported_arches_edit_new"]
        elif choice_result_supported_arches_choice == "Remove":
            value_to_be_removed = prompt(edit_menu_breed_version_supported_arches_delete)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_arches.remove(value_to_be_removed["edit_menu_breed_version_supported_arches_delete"])
        else:
            print("Unknown option selected.")
        # TODO: Validation of arches (only with warning)
    elif choice_edit_information_os_version == "supported_repo_breeds":
        result_repo_breeds_choice = prompt(edit_menu_version_add_remove_edit)
        choice_result_repo_breeds_choice = result_repo_breeds_choice.get("edit_menu_version_add_remove_edit", "")
        if choice_result_repo_breeds_choice == "Add":
            new_value_supported_repo_breed = prompt(edit_menu_breed_version_supported_repo_breeds_add)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_repo_breeds.append(
                new_value_supported_repo_breed["edit_menu_breed_version_supported_repo_breeds_add"])
        elif choice_result_repo_breeds_choice == "Edit":
            new_value_edit_supported_repo_breeds = prompt(edit_menu_breed_version_supported_repo_breeds_edit)
            index_to_change = os_signatures.osbreeds[breed_index].osversions \
                .get(choice_edit_information_os_version_which_2) \
                .supported_repo_breeds.index(
                new_value_edit_supported_repo_breeds["edit_menu_breed_version_supported_repo_breeds_edit"])
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_repo_breeds[index_to_change] = \
                new_value_edit_supported_repo_breeds["edit_menu_breed_version_supported_repo_breeds_edit_new"]
        elif choice_result_repo_breeds_choice == "Remove":
            value_to_be_removed = prompt(edit_menu_breed_version_supported_repo_breeds_delete)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .supported_repo_breeds.remove(
                value_to_be_removed["edit_menu_breed_version_supported_repo_breeds_delete"])
        else:
            print("Unknown option selected.")
        # TODO: Validation for choices (only with warning)
    elif choice_edit_information_os_version == "kernel_file":
        new_value_kernel_file = prompt(edit_menu_breed_version_kernel_file)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).kernel_file \
            = new_value_kernel_file["edit_menu_breed_version_kernel_file"]
    elif choice_edit_information_os_version == "initrd_file":
        new_value_initrd_file = prompt(edit_menu_breed_version_initrd_file)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).kernel_file \
            = new_value_initrd_file["edit_menu_breed_version_initrd_file"]
    elif choice_edit_information_os_version == "isolinux_ok":
        new_value_isolinux_ok = prompt(edit_menu_breed_version_isolinux_ok)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).isolinux_ok \
            = new_value_isolinux_ok["edit_menu_breed_version_isolinux_ok"]
    elif choice_edit_information_os_version == "default_autoinstall":
        # TODO: Filename validation
        new_value_default_autoinstall = prompt(edit_menu_breed_version_default_autoinstall)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
            .default_autoinstall = new_value_default_autoinstall["edit_menu_breed_version_default_autoinstall"]
    elif choice_edit_information_os_version == "kernel_options":
        new_value_kernel_options = prompt(edit_menu_breed_version_kernel_options)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2).kernel_options \
            = new_value_kernel_options["edit_menu_breed_version_kernel_options"]
    elif choice_edit_information_os_version == "kernel_options_post":
        new_value_kernel_options_post = prompt(edit_menu_breed_version_kernel_options_post)
        os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
            .kernel_options_post = new_value_kernel_options_post["edit_menu_breed_version_kernel_options_post"]
    elif choice_edit_information_os_version == "boot_files":
        result_boot_files_choice = prompt(edit_menu_version_add_remove_edit)
        choice_result_boot_files_choice = result_boot_files_choice.get("edit_menu_version_add_remove_edit", "")
        if choice_result_boot_files_choice == "Add":
            new_value_boot_files_add = prompt(edit_menu_breed_version_boot_files_add)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .boot_files.append(new_value_boot_files_add["edit_menu_breed_version_boot_files_add"])
        elif choice_result_boot_files_choice == "Edit":
            new_value_edit_boot_files = prompt(edit_menu_breed_version_boot_files_edit)
            index_to_change = os_signatures.osbreeds[breed_index].osversions \
                .get(choice_edit_information_os_version_which_2) \
                .boot_files.index(new_value_edit_boot_files["edit_menu_breed_version_boot_files_edit"])
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .boot_files[index_to_change] = new_value_edit_boot_files["edit_menu_breed_version_boot_files_edit_new"]
        elif choice_result_boot_files_choice == "Remove":
            value_to_be_removed = prompt(edit_menu_breed_version_boot_files_delete)
            os_signatures.osbreeds[breed_index].osversions.get(choice_edit_information_os_version_which_2) \
                .boot_files.remove(value_to_be_removed["edit_menu_breed_version_boot_files_delete"])
        else:
            print("Unknown option selected.")
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
        result_main_menu = prompt(main_menu_questions)
        chosen_option = result_main_menu.get("main_menu", "")
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
