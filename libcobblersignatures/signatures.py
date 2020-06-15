import json
import urllib.request
from enum import Enum
from json import JSONDecodeError
from typing import List

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

    @property
    def signaturesjson(self):
        return self._signaturesjson

    @signaturesjson.setter
    def signaturesjson(self, value):
        try:
            json.loads(value)
            self._signaturesjson = value
        except JSONDecodeError:
            pass

    @property
    def osbreeds(self):
        return self._osbreeds

    @osbreeds.setter
    def osbreeds(self, value):
        self._osbreeds = value

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
            self.signaturesjson = source
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
        self.signaturesjson = filecontent

    def _importsignaturesurl(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        self.signaturesjson = data.decode('utf-8')

    def _importsignaturesjson(self, jsonobject):
        print("Import them from a json object")
        self._signaturesjson = jsonobject

    def exportsignatures(self, export_type, target=""):
        print("Export")

    def jsontomodels(self):
        print("Convert a valid json into our models.")

    def modelstojson(self):
        print("Convert a valid model into a json.")

    def addosbreed(self, name):
        self._osbreeds.append(OsBreed(name))

    def addosversion(self):
        print("Add a version of a os to an existing group.")

    def removeosbreed(self, index):
        self._osbreeds.remove(index)

    def removeosversion(self):
        print("Remove a version from an existing group")
