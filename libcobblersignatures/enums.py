"""
This module contains all enums which are used in the library.
"""

from enum import Enum


class OsArchitectures(Enum):
    """
    An enumeration which defines the in Cobbler available architectures.
    """

    i386 = 1
    """
    32-bit architecture which is also called ``IA-32`` or ``80x86`` by some people.
    """
    x86_64 = 2
    """
    64-bit architecture which is also called ``x64``, ``x86-64``, ``AMD64`` or ``amd64``.
    """
    ppc = 3
    """
    32-bit big-endian PowerPC architecture.
    """
    ppc64 = 4
    """
    64-bit big-endian PowerPC architecture.
    """
    amd64 = 5
    """
    Synonym for ``x86_64``.
    """


class RepositoryBreeds(Enum):
    """
    An enumeration which defines the in Cobbler available repository breeds.
    """

    rsync = 1
    """
    A repository which is synced by rsync.
    """
    rhn = 2
    """
    A repository type from Red Hat which can be used by yum.
    """
    yum = 3
    """
    A repository which is manged by yum.
    """
    apt = 4
    """
    A repository which is managed by apt.
    """


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
