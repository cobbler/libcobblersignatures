class OsBreed:
    def __init__(self):
        self._name = ""
        self._osversions = {}

    @property
    def osversions(self):
        return self._osversions

    @osversions.setter
    def osversions(self, value):
        self._osversions = value

    @osversions.deleter
    def osversions(self):
        del self._osversions

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    def osversion_add(self, version, index):
        if index is None:
            self.osversions.append(version)
        else:
            self.osversions.insert(version, index)
        self.osversions.sort()

    def osversion_remove(self, index):
        self.osversions.remove(index)