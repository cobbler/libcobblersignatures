from enum import Enum


class ImportTypes(Enum):
    FILE = 0
    URL = 1
    STRING = 2


class ExportTypes(Enum):
    FILE = 0
    STRING = 1


class Signatures:

    def __init__(self):
        print("Test")

    def createemptysignatures(self):
        print("Start from scratch.")

    def importsignatures(self, import_type):
        print("Import")

    def exportsignatures(self, export_type):
        print("Export")

    def validatejsonsyntax(self):
        print("Check syntax of json read from string or file.")

    def jsontomodels(self):
        print("Convert a valid json into our models.")

    def modelstojson(self):
        print("Convert a valid model into a json.")

    def addosbreed(self):
        print("Add a operating system group.")

    def addosversion(self):
        print("Add a version of a os to an existing group.")

    def removeosbreed(self):
        print("Remove a os group")

    def removeosversion(self):
        print("Remove a version from an existing group")
