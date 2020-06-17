from PyInquirer import prompt

from libcobblersignatures.signatures import Signatures

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


def main_menu():
    return prompt(main_menu_questions)


def import_menu():
    return prompt(import_menu_questions)


def export_menu():
    return prompt(export_menu_questions)


def edit_menu():
    return prompt(edit_menu_questions)


def main():
    main_menu_option_selected = 0
    while main_menu_option_selected != 3:
        result_main_menu = main_menu()
        if result_main_menu["main_menu"] == "Import":
            main_menu_option_selected = 0
            print("Import")
            result_import_menu = import_menu()
        elif result_main_menu["main_menu"] == "Export":
            main_menu_option_selected = 1
            print("Export")
            result_export_menu = export_menu()
        elif result_main_menu["main_menu"] == "Edit":
            main_menu_option_selected = 2
            print("Edit")
            result_edit_menu = edit_menu()
        elif result_main_menu["main_menu"] == "Exit":
            main_menu_option_selected = 3
            print("Exit")
    exit(0)


if __name__ == "__main__":
    main()
