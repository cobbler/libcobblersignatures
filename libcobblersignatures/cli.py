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
    names = []
    for v in os_signatures.osbreeds:
        names.append(v.name)
    return names


def update_os_breed_choices(question):
    question[0].update({"choices": get_os_breed_names().append("Go Back")})


def import_menu():
    result_import_menu = prompt(import_menu_questions)
    if result_import_menu["import_menu_source"] in ["URL", "File", "String"]:
        result_import_menu_2 = prompt(import_menu_questions2)
        if result_import_menu["import_menu_source"] == "URL":
            import_type = ImportTypes.URL
        elif result_import_menu["import_menu_source"] == "File":
            import_type = ImportTypes.FILE
        elif result_import_menu["import_menu_source"] == "String":
            import_type = ImportTypes.STRING
        else:
            return
        os_signatures.importsignatures(import_type, result_import_menu_2["import_menu_signatures"])


def export_menu():
    result_export_menu = prompt(export_menu_questions)
    if result_export_menu["export_menu_sources"] in ["String", "File"]:
        if result_export_menu["export_menu_sources"] == "String":
            os_signatures.modelstojson()
            print(os_signatures.exportsignatures(ExportTypes.STRING))
        elif result_export_menu["export_menu_sources"] == "File":
            result_export_menu_2 = prompt(export_menu_questions2)
            os_signatures.modelstojson()
            os_signatures.exportsignatures(ExportTypes.FILE, result_export_menu_2["export_menu_signatures"])
        else:
            return


def edit_menu():
    global os_signatures
    result_edit_menu = prompt(edit_menu_questions)
    if result_edit_menu["edit_main_menu"] == "Add Operating System Breed":
        result_edit_add_os_breed = prompt(edit_add_os_breed)
        os_signatures.addosbreed(result_edit_add_os_breed["edit_add_os_breed"])
        print("We now have %s Operating System Breeds in this file." % len(os_signatures.osbreeds))
    elif result_edit_menu["edit_main_menu"] == "Remove Operating System Breed":
        update_os_breed_choices(edit_remove_os_breed)
        result_edit_remove_os_breed = prompt(edit_remove_os_breed)
        for index in [0, len(os_signatures.osbreeds)]:
            if result_edit_remove_os_breed["edit_remove_os_breed"] == os_signatures.osbreeds[index]:
                os_signatures.removeosbreed(index)
                break
            else:
                print("Operating System Breed not found. Doing nothing.")
    elif result_edit_menu["edit_main_menu"] == "Edit the name of an Operating System Breed":
        update_os_breed_choices(edit_name_os_breed_1)
        result_edit_name_os_breed_1 = prompt(edit_name_os_breed_1)
        for index in [0, len(os_signatures.osbreeds)]:
            if result_edit_name_os_breed_1["edit_name_os_breed_1"] == os_signatures.osbreeds[index]:
                result_edit_name_os_breed_2 = prompt(edit_name_os_breed_2)
                os_signatures.osbreeds[index].name = result_edit_name_os_breed_2["edit_name_os_breed_2"]
                break
            else:
                print("Operating System Breed not found. Doing nothing.")
    elif result_edit_menu["edit_main_menu"] == "Add Operating System Version":
        update_os_breed_choices(edit_add_os_version_1)
        result_edit_add_os_version_1 = prompt(edit_add_os_version_1)
        for index in [0, len(os_signatures.osbreeds)]:
            if result_edit_add_os_version_1["edit_add_os_version_1"] == os_signatures.osbreeds[index]:
                result_edit_add_os_version_2 = prompt(edit_add_os_version_2)
                os_signatures.addosversion(index, result_edit_add_os_version_2["edit_add_os_version_2"], None)
                break
            else:
                print("Operating System Breed not found. Doing nothing.")
    elif result_edit_menu["edit_main_menu"] == "Remove Operating System Version":
        update_os_breed_choices(edit_remove_os_version_1)
        result_edit_remove_os_version_1 = prompt(edit_remove_os_version_1)
        for index in [0, len(os_signatures.osbreeds)]:
            if result_edit_remove_os_version_1["edit_remove_os_version_1"] == os_signatures.osbreeds[index]:
                result_edit_remove_os_version_2 = prompt(edit_remove_os_version_2)
                os_signatures.removeosversion(index, result_edit_remove_os_version_2["edit_remove_os_version_2"])
                break
            else:
                print("Operating System Breed not found. Doing nothing.")
    elif result_edit_menu["edit_main_menu"] == "Edit the information of an Operating System Version":
        edit_menu_breed_version_info()
    elif result_edit_menu["edit_main_menu"] == "Start from scratch":
        os_signatures = Signatures()
    elif result_edit_menu["edit_main_menu"] == "Go Back":
        return


def edit_menu_breed_version_info():
    edit_information_os_version_which_result = prompt(edit_information_os_version_which)
    # TODO: Update next prompot to preview values
    result_edit_information_os_version = prompt(edit_information_os_version)
    if result_edit_information_os_version["edit_information_os_version"] == "signatures":
        # TODO: Add/Remove/Edit for Array
        result_signatures_choice = prompt(edit_menu_version_add_remove_edit)
        if result_signatures_choice["edit_menu_version_add_remove_edit"] == "Add":
            prompt(edit_menu_breed_version_signatures_add)
        elif result_signatures_choice["edit_menu_version_add_remove_edit"] == "Edit":
            prompt(edit_menu_breed_version_signatures_edit)
        elif result_signatures_choice["edit_menu_version_add_remove_edit"] == "Remove":
            prompt(edit_menu_breed_version_signatures_delete)
        else:
            print("Unknown option selected.")
    elif result_edit_information_os_version["edit_information_os_version"] == "version_file":
        # TODO: String Input
        prompt(edit_menu_breed_version_version_file)
    elif result_edit_information_os_version["edit_information_os_version"] == "version_file_regex":
        # TODO: String Input
        prompt(edit_menu_breed_version_version_file_regex)
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_arch":
        # TODO: String Input
        prompt(edit_menu_breed_version_kernel_arch)
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_arch_regex":
        # TODO: String Input
        prompt(edit_menu_breed_version_kernel_arch_regex)
    elif result_edit_information_os_version["edit_information_os_version"] == "supported_arches":
        # TODO: Add/Remove/Edit for Array
        result_supported_arches_choice = prompt(edit_menu_version_add_remove_edit)
        if result_supported_arches_choice["edit_menu_version_add_remove_edit"] == "Add":
            prompt(edit_menu_breed_version_supported_arches_add)
        elif result_supported_arches_choice["edit_menu_version_add_remove_edit"] == "Edit":
            prompt(edit_menu_breed_version_supported_arches_edit)
        elif result_supported_arches_choice["edit_menu_version_add_remove_edit"] == "Remove":
            prompt(edit_menu_breed_version_supported_arches_delete)
        else:
            print("Unknown option selected.")
        # TODO: Validation of arches (only with warning)
    elif result_edit_information_os_version["edit_information_os_version"] == "supported_repo_breeds":
        # TODO: Add/Remove/edit for Array
        result_repo_breeds_choice = prompt(edit_menu_version_add_remove_edit)
        if result_repo_breeds_choice["edit_menu_version_add_remove_edit"] == "Add":
            prompt(edit_menu_breed_version_supported_repo_breeds_add)
        elif result_repo_breeds_choice["edit_menu_version_add_remove_edit"] == "Edit":
            prompt(edit_menu_breed_version_supported_repo_breeds_edit)
        elif result_repo_breeds_choice["edit_menu_version_add_remove_edit"] == "Remove":
            prompt(edit_menu_breed_version_supported_repo_breeds_delete)
        else:
            print("Unknown option selected.")
        # TODO: Validation for choices (only with warning)
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_file":
        # TODO: String Input
        prompt(edit_menu_breed_version_kernel_file)
    elif result_edit_information_os_version["edit_information_os_version"] == "initrd_file":
        # TODO: String Input
        prompt(edit_menu_breed_version_initrd_file)
    elif result_edit_information_os_version["edit_information_os_version"] == "isolinux_ok":
        # TODO: Boolean Question
        prompt(edit_menu_breed_version_isolinux_ok)
    elif result_edit_information_os_version["edit_information_os_version"] == "default_autoinstall":
        # TODO: String Input with filename validation
        prompt(edit_menu_breed_version_default_autoinstall)
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_options":
        # TODO: String Input
        prompt(edit_menu_breed_version_kernel_options)
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_options_post":
        # TODO: String Input
        prompt(edit_menu_breed_version_kernel_options_post)
    elif result_edit_information_os_version["edit_information_os_version"] == "boot_files":
        # TODO: Add/Remove/Edit for Array
        result_boot_files_choice = prompt(edit_menu_version_add_remove_edit)
        if result_boot_files_choice["edit_menu_version_add_remove_edit"] == "Add":
            prompt(edit_menu_breed_version_boot_files_add)
        elif result_boot_files_choice["edit_menu_version_add_remove_edit"] == "Edit":
            prompt(edit_menu_breed_version_boot_files_edit)
        elif result_boot_files_choice["edit_menu_version_add_remove_edit"] == "Remove":
            prompt(edit_menu_breed_version_boot_files_delete)
        else:
            print("Unknown option selected.")
    else:
        return


def main():
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
