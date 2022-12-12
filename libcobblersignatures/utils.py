"""
Helper methods which are not directly related to any class or module in this library.
"""

from typing import Union


def convert_none_to_default(
    value: Union[str, int, bool, list, dict, set, None], value_type
) -> Union[str, int, bool, list, dict, set, None]:
    """
    This method checks if the value handed to it is ``None``, otherwise the default value for the type will be returned.

    :param value: The value which should be checked.
    :param value_type: The type which should be returned in case the value is ``None``!
    :return: The default value. Int: 0; str: ""; bool: False; list: []; dict: {}; set: ``set()``
    :raises TypeError: In case an unknown type was selected.
    """
    if value is not None:
        return value
    if value_type == str:
        return ""
    elif value_type == int:
        return 0
    elif value_type == bool:
        return False
    elif value_type == list:
        return []
    elif value_type == dict:
        return {}
    elif value_type == set:
        return set()
    else:
        raise TypeError("The type you supplied for value_type was not known.")
