import json
import urllib.request
from enum import Enum
from json import JSONDecodeError
from typing import List

from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


class ImportTypes(Enum):
    """
    An enumeration which defines the possible sources for importing the JSON file.
    """
    FILE = 0
    """
    This value shall be given when the content shall be imported from a file on a file system which is locally
    accessible.
    """
    URL = 1
    """
    This value shall be given when the content shall be imported from a URL.
    """
    STRING = 2
    """
    This value shall be given when the content shall be imported from a string. This string shall not contain any
    linebreaks.
    """
    JSON = 3
    """
    This value shall be given when the content shall be imported from a Python JSON object. This is only useful for
    Python Code.
    """


class ExportTypes(Enum):
    """
    An enumeration which defines the possible export targets for the JSON file.
    """
    FILE = 0
    """
    This value shall be given when the content of the manipulated content shall be exported to a file.
    """
    STRING = 1
    """
    This value shall be given when the content of the manipulated content shall be exported to a String which is
    outputted to the shell.
    """


class Signatures:
    """
    This is the entry point of the library. You may create one or more objects of this class. Each instance of it is
    independent of the other. I recommend only to have on object at a time of this class. This library doesn't persist
    anything except you explicitly use the export method of the instance.
    """

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
        """
        This property represents the json which was im- or exported.

        :return: The last valid content of the json which the library knows about.
        """
        return self._signaturesjson

    @signaturesjson.setter
    def signaturesjson(self, value):
        try:
            self._signaturesjson = json.loads(value)
        except JSONDecodeError:
            pass

    @property
    def osbreeds(self):
        """
        This property represents the currently manipulated data structures.

        :return: The list with the content which is currently manipulated.
        """
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
        """
        Internal function to handle the import of a file based import.

        :param filepath: The relative or absolute path. Additionally this may be all path variations which are accepted
                         by the Python ``open()`` function.
        """
        with open(filepath) as f:
            filecontent = f.read()
        if filecontent is None:
            raise FileNotFoundError("Filecontent was not correctly read!")
        self.signaturesjson = filecontent

    def _importsignaturesurl(self, url):
        """
        Internal function to handle the import of a URL based import. The data behind it should be a well formed JSON.

        :param url: The URL to load the content from. This parameter is handed to urllib.
        """
        response = urllib.request.urlopen(url)
        data = response.read()
        self.signaturesjson = data.decode('utf-8')

    def _importsignaturesjson(self, jsonobject):
        """
        Internal function to handle the import of a direct JSON based approach.

        :param jsonobject: The JSON Object to set as the signatures.
        """
        self.signaturesjson = jsonobject

    def exportsignatures(self, export_type, target=""):
        """
        This is the main export function.

        :param export_type: One of the values from the :class:`ExportTypes`.
        :param target: This is only required when using this for a file based export. Otherwise this can be skipped.
        :raises ValueError: When the :class:`ExportTypes` is not implemented or not known.
        """
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
        """
        Convert the loaded JSON to the internal modules. Without calling this the loaded data will not be available for
        manipulation.
        """
        breeds = self.signaturesjson.get(self._rootkey, -1)
        if breeds == -1:
            raise AttributeError("Missing Rootkey \"" + self._rootkey + "\".")
        for key in breeds:
            breed = OsBreed(key)
            breed.decode(breeds[key])
            self.osbreeds.append(breed)

    def modelstojson(self):
        """
        Convert the internal data to a JSON. Without calling this the created and manipulated content will not be
        available for im- and export.
        """
        value = {}
        for breed in self.osbreeds:
            value[breed.name] = breed.encode()
        self.signaturesjson = json.dumps({self._rootkey: value})

    def addosbreed(self, name: str):
        """
        Add a new :class:`OsBreed`.

        :param name: The name of the new breed. Must not exist in the currently loaded models.
        """
        self.osbreeds.append(OsBreed(name))

    def addosversion(self, breedindex: int, versionname: str, versiondata):
        """
        Add a new :class:`Osversion`.

        :param breedindex: The index of the operating system breed. This can be found by using
                           ``get_breed_index_by_name()``.
        :param versionname: The name of the new version.
        :param versiondata: The object with the data of the version to add. If this is ``None`` then an empty version
                            will be created.
        """
        if versiondata is None:
            versiondata = Osversion()
        self.osbreeds[breedindex].osversion_add(versionname, versiondata)

    def removeosbreed(self, index: int):
        """
        Remove an operating system breed via its index. All nested content will be removed.

        :param index: The index which will be removed.
        """
        if index >= len(self.osbreeds):
            raise ValueError("Index out of Range")
        del self.osbreeds[index]

    def removeosversion(self, breedindex: int, versionname: str):
        """
        Remove a single operating system version.

        :param breedindex: The index of the operating system breed index.
        :param versionname: The name of the version to remove.
        """
        self.osbreeds[breedindex].osversion_remove(versionname)

    def get_breed_index_by_name(self, name: str) -> int:
        """
        Searches with the name of the :class:`OsBreed` for the index.

        :param name: The name of the :class:`OsBreed` to look for.
        :return: The number of the index or ``-1``.
        """
        list_length = len(self.osbreeds)
        if list_length > 0:
            for index in range(list_length):
                if name == self.osbreeds[index].name:
                    return index
        return -1
