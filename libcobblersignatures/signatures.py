import json
import urllib.request
from enum import Enum
from json import JSONDecodeError
from typing import List

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


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
            self._signaturesjson = json.loads(value)
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
        self.signaturesjson = jsonobject

    def exportsignatures(self, export_type, target=""):
        if self.signaturesjson is None:
            raise ValueError("No Signatures to export.")
        if export_type == ExportTypes.FILE:
            if not target:
                raise ValueError("Please provide a path if your want to export to a file!")
            with open(target, "w") as f:
                f.write(json.dumps(self.signaturesjson))
        elif export_type == ExportTypes.STRING:
            return json.dumps(self.signaturesjson)
        else:
            raise ValueError("Please use on of the four given options for the export type!")

    def jsontomodels(self):
        breeds = self.signaturesjson.get(self._rootkey, -1)
        if breeds == -1:
            raise AttributeError("Missing Rootkey \"" + self._rootkey + "\".")
        for key in breeds:
            breed = OsBreed(key)
            breed.decode(breeds[key])
            self.osbreeds.append(breed)

    def modelstojson(self):
        value = {}
        for breed in self.osbreeds:
            value[breed.name] = breed.encode()
        self.signaturesjson = json.dumps({self._rootkey: value})

    def addosbreed(self, name):
        self.osbreeds.append(OsBreed(name))

    def addosversion(self, breedindex, versionname, versiondata):
        if versiondata is None:
            versiondata = Osversion()
        self.osbreeds[breedindex].osversion_add(versionname, versiondata)

    def removeosbreed(self, index: int):
        if index >= len(self.osbreeds):
            raise ValueError("Index out of Range")
        del self.osbreeds[index]

    def removeosversion(self, breedindex, versionname):
        self.osbreeds[breedindex].osversion_remove(versionname)

    def get_breed_index_by_name(self, name):
        list_length = len(self.osbreeds)
        if list_length > 0:
            for index in range(list_length):
                if name == self.osbreeds[index].name:
                    return index
        return -1
