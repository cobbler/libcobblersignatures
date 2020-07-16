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
    result_edit_information_os_version = prompt(edit_information_os_version)
    if result_edit_information_os_version["edit_information_os_version"] == "signatures":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "version_file":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "version_file_regex":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_arch":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_arch_regex":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "supported_arches":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "supported_repo_breeds":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_file":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "initrd_file":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "isolinux_ok":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "default_autoinstall":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_options":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "kernel_options_post":
        pass
    elif result_edit_information_os_version["edit_information_os_version"] == "boot_files":
        pass
    else:
        pass


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
