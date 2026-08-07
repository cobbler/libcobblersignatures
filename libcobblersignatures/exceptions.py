"""
This module contains all exceptions which are raised by this library. All of them derive from :class:`SignaturesError`
so callers can catch a single type for anything going wrong in this library, while each also derives from the builtin
exception type it replaces so existing callers relying on that type keep working.
"""


class SignaturesError(Exception):
    """
    Base class for all errors raised by this library.
    """


class SignaturesImportError(SignaturesError, OSError):
    """
    Raised when a signatures source (a file or a URL) could not be read.
    """


class SignaturesParseError(SignaturesError, ValueError):
    """
    Raised when the source content was not valid JSON.
    """


class SignaturesValidationError(SignaturesError, ValueError):
    """
    Raised when the JSON was syntactically valid but structurally wrong, e.g. a missing rootkey or a field with the
    wrong type.
    """


class SignaturesExportError(SignaturesError, OSError):
    """
    Raised when signatures data could not be written to the export target.
    """
