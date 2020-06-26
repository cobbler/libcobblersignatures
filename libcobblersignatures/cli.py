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
        "name": "main_menu",
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
        ]
    }
]


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
        result_export_menu_2 = prompt(export_menu_questions2)
        if result_export_menu["export_menu_sources"] == "String":
            os_signatures.exportsignatures(ExportTypes.STRING)
        elif result_export_menu["export_menu_sources"] == "File":
            os_signatures.exportsignatures(ExportTypes.FILE, result_export_menu_2["export_menu_signatures"])
        else:
            return


def edit_menu():
    result_edit_menu = prompt(edit_menu_questions)
    if result_edit_menu:
        pass
    else:
        return


def main():
    main_menu_option_selected = 0
    while main_menu_option_selected != 3:
        result_main_menu = prompt(main_menu_questions)
        if result_main_menu["main_menu"] == "Import":
            main_menu_option_selected = 0
            import_menu()
        elif result_main_menu["main_menu"] == "Export":
            main_menu_option_selected = 1
            export_menu()
        elif result_main_menu["main_menu"] == "Edit":
            main_menu_option_selected = 2
            edit_menu()
        elif result_main_menu["main_menu"] == "Exit":
            main_menu_option_selected = 3
            print("Any progress which is not exported will be lost. Bye.")
    exit(0)


if __name__ == "__main__":
    main()
