"""
Helper methods which are not directly related to any class or module in this library.
"""

from typing import Optional, Type, TypeVar, cast

T = TypeVar("T", str, int, bool, list, dict, set)


def convert_none_to_default(value: Optional[T], value_type: Type[T]) -> T:
    """
    This method checks if the value handed to it is ``None``, otherwise the default value for the type will be returned.

    :param value: The value which should be checked.
    :param value_type: The type which should be returned in case the value is ``None``!
    :return: The default value. Int: 0; str: ""; bool: False; list: []; dict: {}; set: ``set()``
    :raises TypeError: In case an unknown type was selected.
    """
    if value is not None:
        return value
    if value_type is str:
        return cast(T, "")
    elif value_type is int:
        return cast(T, 0)
    elif value_type is bool:
        return cast(T, False)
    elif value_type is list:
        return cast(T, [])
    elif value_type is dict:
        return cast(T, {})
    elif value_type is set:
        return cast(T, set())
    else:
        raise TypeError("The type you supplied for value_type was not known.")
