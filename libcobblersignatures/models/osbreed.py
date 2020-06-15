import collections


class OsBreed:

    def __init__(self, name):
        self._name = name
        self._osversions = collections.OrderedDict()

    @property
    def osversions(self):
        return self._osversions

    @osversions.setter
    def osversions(self, value):
        self._osversions = value

    @osversions.deleter
    def osversions(self):
        self._osversions = collections.OrderedDict()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise TypeError("Name cannot be an empty string.")
        else:
            self._name = value

    @name.deleter
    def name(self):
        raise TypeError("The name of this error cannot be deleted.")

    def osversion_add(self, name, version):
        self.osversions[name] = version

    def osversion_remove(self, key):
        self.osversions.pop(key)
