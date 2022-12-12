import collections

from libcobblersignatures.models.osversion import Osversion


class OsBreed:
    """
    On operating system breed like SUSE or Redhat. The specification of the attributes and what values are valid are
    described in the JSON specification.
    """

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("The name of an OsBreed must be of type str!")
        self._name = name
        self._osversions = collections.OrderedDict()

    def __eq__(self, other):
        if not isinstance(other, OsBreed):
            return NotImplemented
        return self.name == other.name and self.osversions == other.osversions

    @property
    def osversions(self) -> collections.OrderedDict:
        """
        An ordered dictionary which contains all versions of the operating system breed.

        :setter: Raises a TypeError in case the value is not an OrderedDict.
        :getter: The ordered dictionary.
        :deleter: Will reset the number of versions to an empty list.
        """
        return self._osversions

    @osversions.setter
    def osversions(self, value: collections.OrderedDict):
        """
        The setter of the osversions dictionary.

        :param value: The dictionary which contains all osversions models.
        """
        if not isinstance(value, collections.OrderedDict):
            raise TypeError("The osversion needs to be an ordered dict!")
        self._osversions = value

    @osversions.deleter
    def osversions(self):
        """
        Resets the os versions to an empty ordered dict.
        """
        self._osversions = collections.OrderedDict()

    @property
    def name(self):
        """
        This property represents the name of the operating system breed.

        :setter: Invalid values will be discarded.
        :deleter: Always raises a TypeError since this is not allowed.
        :getter: The last successfully validated name of the operating system breed.
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        The setter of the name for an OsBreed.

        :param value: The name of the breed.
        """
        if not value:
            raise TypeError("Name cannot be an empty string.")
        else:
            self._name = value

    @name.deleter
    def name(self):
        """
        This is a forbidden action. Thus always raising.

        :raises TypeError: In case the name is tried to be deleted.
        """
        raise TypeError("The name of this error cannot be deleted.")

    def encode(self) -> dict:
        """
        Encodes the current OsBreed and nested Osversions.

        :return: The dictionary with all its versions. The name of the OsBreed is not included as this is normally the
                 name of the returned key.
        """
        versionsdict = {}
        for name in self.osversions:
            versionsdict.update({name: self.osversions[name].encode()})
        return versionsdict

    def decode(self, data: dict):
        """
        Decodes the received data. Decoding of each single version is done by the corresponding decode method in
        :class:`Osversion`.

        :param data: The data to decode.
        """
        for key in data.keys():
            version = Osversion()
            version.decode(data.get(key))
            self.osversion_add(key, version)

    def osversion_add(self, name: str, version: Osversion):
        """
        Add an Osversion to this OsBreed.

        :param name: The name of the version to add.
        :param version: The Osversion to add to the OsBreed.
        :raises ValueError: If the Name is not a ``str`` and/or the Version is not an ``Osversion``.
        """
        if isinstance(name, str) and isinstance(version, Osversion):
            if name in self.osversions:
                raise ValueError(
                    'The name "%s" already exists for the OsBreed "%s"!'
                    % (name, self.name)
                )
            self.osversions[name] = version
        else:
            raise ValueError("Name must be str and Version must be Osversion.")

    def osversion_remove(self, key: str):
        """
        Remove an Osversion with its key.

        :param key: The key of the dictionary to remove.
        """
        self.osversions.pop(key)
