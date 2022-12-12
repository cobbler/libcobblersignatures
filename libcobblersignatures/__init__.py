"""
This library contains additionally a CLI which enables you to have a feature equal way to manipulate the objects, as
well as to im- and export them.
"""

import json
import urllib.request
from typing import List, Union

from libcobblersignatures.enums import ExportTypes, ImportTypes
from libcobblersignatures.models.osbreed import OsBreed
from libcobblersignatures.models.osversion import Osversion


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

        :raises JSONDecodeError: If invalid json is given
        :return: The last valid content of the json which the library knows about.
        """
        return self._signaturesjson

    @signaturesjson.setter
    def signaturesjson(self, value: str):
        """
        The setter for the exported data structure.

        :param value: The str which will be loaded by the Python json utility.
        """
        if value is None:
            return
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
            raise ValueError("Please use on of the four given options for the source!")

    def _importsignaturesfile(self, filepath: str):
        """
        Internal function to handle the import of a file based import.

        :param filepath: The relative or absolute path. Additionally this may be all path variations which are accepted
                         by the Python ``open()`` function.
        """
        with open(filepath, "r") as f:
            self.signaturesjson = f.read()

    def _importsignaturesurl(self, url: str):
        """
        Internal function to handle the import of a URL based import. The data behind it should be a well formed JSON.

        :param url: The URL to load the content from. This parameter is handed to urllib.
        """
        response = urllib.request.urlopen(url)
        data = response.read()
        self.signaturesjson = data.decode("utf-8")

    def __prepare_export_output(
        self, sort_keys: bool = False, indent: Union[None, int] = None
    ) -> str:
        """
        Convert the internal data to a JSON. Only for internal usage.

        :param sort_keys: If the keys of the dictionary should be sorted to be more human readable.
        :param indent: If this is something other then ``None`` then the JSON will be pretty printed.
        """
        value = {breed.name: breed.encode() for breed in self.osbreeds}
        return json.dumps({self._rootkey: value}, sort_keys=sort_keys, indent=indent)

    def exportsignatures(
        self,
        export_type: ExportTypes,
        target: str = "",
        sort_keys: bool = False,
        indent: Union[None, int] = None,
    ):
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
                raise ValueError(
                    "Please provide a path if your want to export to a file!"
                )
            with open(target, "w") as f:
                f.write(self.__prepare_export_output(sort_keys, indent))
        elif export_type == ExportTypes.STRING:
            return self.__prepare_export_output(sort_keys, indent)
        else:
            raise ValueError(
                "Please use on of the two given options for the export type!"
            )

    def jsontomodels(self):
        """
        Convert the loaded JSON to the internal modules. Without calling this the loaded data will not be available for
        manipulation.
        """
        missing_rootkey = object()
        breeds = self.signaturesjson.get(self._rootkey, missing_rootkey)
        if breeds is missing_rootkey:
            raise AttributeError('Missing Rootkey "' + self._rootkey + '".')
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
            raise ValueError('Breed "%s" already in the list of breeds!' % name)
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
