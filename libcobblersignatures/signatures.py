import json
import urllib.request
from enum import Enum
from typing import List, Union

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
    _signaturesjson: dict
    _osbreeds: List[OsBreed]

    def __init__(self):
        """
        If you want to create an empty file just use this constructor. If you want to import one use this and then run
        an import function.
        """
        self._rootkey = "breeds"
        self._signaturesjson = {}
        self._osbreeds = []

    @property
    def signaturesjson(self) -> dict:
        """
        This property represents the json which was im- or exported.

        :getter: The last valid content of the json which the library knows about.
        :setter: May raise a JSONDecodeError in case an invalid json document is given.
        """
        return self._signaturesjson

    @signaturesjson.setter
    def signaturesjson(self, value: str):
        """
        The setter for the exported data structure.

        :param value: The str which will be loaded by the Python json utility.
        :raises JSONDecodeError: In case the value was not a valid JSON document.
        """
        if value is None:
            pass
        self._signaturesjson = json.loads(value)

    @property
    def osbreeds(self) -> List[OsBreed]:
        """
        This property represents the currently manipulated data structures.

        :return: The list with the content which is currently manipulated.
        """
        return self._osbreeds

    @osbreeds.setter
    def osbreeds(self, value: List[OsBreed]):
        """
        The setter for the osbreeds property.

        :param value: The list with the OsBreeds.
        """
        self._osbreeds = value

    def importsignatures(self, import_type: ImportTypes, source: str):
        """
        This is the main import function.

        :param import_type: This is one of the four options from the ImportTypes Enum
        :param source: A string containing the data to be parsed into a json in the end
        """
        # TODO make sure source is never none and reasonable
        if import_type == ImportTypes.FILE:
            self._importsignaturesfile(source)
        elif import_type == ImportTypes.URL:
            self._importsignaturesurl(source)
        elif import_type == ImportTypes.STRING:
            self.signaturesjson = source
        else:
            raise ValueError("Please use one of the four given options for the source!")

    def _importsignaturesfile(self, filepath: str):
        """
        Internal function to handle the import of a file based import.

        :param filepath: The relative or absolute path. Additionally this may be all path variations which are accepted
                         by the Python ``open()`` function.
        """
        with open(filepath, 'r') as f:
            self.signaturesjson = f.read()

    def _importsignaturesurl(self, url: str):
        """
        Internal function to handle the import of a URL based import. The data behind it should be a well formed JSON.

        :param url: The URL to load the content from. This parameter is handed to urllib.
        """
        response = urllib.request.urlopen(url)
        data = response.read()
        self.signaturesjson = data.decode('utf-8')

    def __prepare_export_output(self, sort_keys: bool = False, indent: Union[None, int] = None) -> str:
        """
        Convert the internal data to a JSON. Only for internal usage.

        :param sort_keys: If the keys of the dictionary should be sorted to be more human readable.
        :param indent: If this is something other then ``None`` then the JSON will be pretty printed.
        """
        value = {}
        for breed in self.osbreeds:
            value[breed.name] = breed.encode()
        return json.dumps({self._rootkey: value}, sort_keys=sort_keys, indent=indent)

    def exportsignatures(self, export_type: ExportTypes, target: str = "", sort_keys: bool = False,
                         indent: Union[None, int] = None):
        """
        This is the main export function.

        :param export_type: One of the values from the :class:`ExportTypes`.
        :param target: This is only required when using this for a file based export. Otherwise this can be skipped.
        :param sort_keys: If the keys of the dictionary should be sorted to be more human readable.
        :param indent: If this is something other then ``None`` then the JSON will be pretty printed.
        :raises ValueError: When the :class:`ExportTypes` is not implemented or not known.
        :raises TypeError: When one of the arguments has the wrong type.
        """
        if not isinstance(target, str):
            raise TypeError("target needs to be of type str!")
        if not isinstance(sort_keys, bool):
            raise TypeError("sort_keys needs to be of type bool!")
        if not (indent is None or isinstance(indent, int)):
            raise TypeError("indent needs to be of type integer or None!")

        if export_type == ExportTypes.FILE:
            if not target:
                raise ValueError("Please provide a path if your want to export to a file!")
            with open(target, "w") as f:
                f.write(self.__prepare_export_output(sort_keys, indent))
        elif export_type == ExportTypes.STRING:
            return self.__prepare_export_output(sort_keys, indent)
        else:
            raise ValueError("Please use one of the two given options for the export type!")

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

    def addosbreed(self, name: str):
        """
        Add a new :class:`OsBreed`.

        :param name: The name of the new breed. Must not exist in the currently loaded models.
        """
        if name in [x.name for x in self.osbreeds]:
            raise ValueError("Breed \"%s\" already in the list of breeds!" % name)
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
