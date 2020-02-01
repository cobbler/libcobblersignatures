from enum import Enum

from libcobblersignatures.models.osbreed import OsBreed


class ImportTypes(Enum):
    FILE = 0
    URL = 1
    STRING = 2
    JSON = 3


class ExportTypes(Enum):
    FILE = 0
    STRING = 1


class Signatures:

    def __init__(self):
        print("Test")
        self._rootkey = "breeds"
        self._signaturesjson = None

    def createemptysignatures(self):
        print("Start from scratch.")
        self._signaturesjson = OsBreed()

    def importsignatures(self, import_type, source):
        print("Import")

    def _importsignaturesfile(self, filepath):
        print("Import the signatures from a file")

    def _importsignaturesurl(self, url):
        print("Download and then import it.")

    def _importsignaturestring(self, jsonstring):
        print("Import from string")

    def _importsignaturesjson(self, jsonobject):
        print("Import them from a json object")

    def exportsignatures(self, export_type, target):
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
