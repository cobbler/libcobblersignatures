from enum import Enum
import json
from typing import List
import urllib.request

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

    _rootkey: str
    _signaturesjson: json
    _osbreeds: List[OsBreed]

    def __init__(self):
        """
        If you want to create an empty file just use this constructor. If you want to import one use this and then run
        an import function.
        """
        self._rootkey = "breeds"
        self._signaturesjson = None
        self._osbreeds = []

    def importsignatures(self, import_type, source):
        """
        This is the main import function.

        :param import_type: This is one of the four options from the ImportTypes Enum
        :type import_type: ImportTypes
        :param source: A string containing the data to be parsed into a json in the end
        :type source: str
        """
        if import_type == ImportTypes.FILE:
            self._importsignaturesfile(source)
        elif import_type == ImportTypes.URL:
            self._importsignaturesurl(source)
        elif import_type == ImportTypes.STRING:
            self._importsignaturestring(source)
        elif import_type == ImportTypes.JSON:
            self._importsignaturesjson(source)
        else:
            raise ValueError("Please use on of the four given options for the source!")

    def _importsignaturesfile(self, filepath):
        filecontent = None
        with open(filepath) as f:
            filecontent = f.read()
        if filecontent is None:
            raise FileNotFoundError("Filecontent was not correctly read!")
        self._importsignaturestring(filecontent)

    def _importsignaturesurl(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        self._importsignaturestring(data.decode('utf-8'))

    def _importsignaturestring(self, jsonstring):
        """
        This decodes a string to a json object. This is done like in the Python Docs described:
        https://docs.python.org/3/library/json.html#json.JSONDecoder

        :param jsonstring: A str which contains the json.
        :type jsonstring: str
        """
        jsondict = json.loads(jsonstring)

    def _importsignaturesjson(self, jsonobject):
        print("Import them from a json object")
        self._signaturesjson = jsonobject

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
