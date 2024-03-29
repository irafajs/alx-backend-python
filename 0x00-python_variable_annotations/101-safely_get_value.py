#!/usr/bin/env python3
"""
Shebang to Create a PY script
"""


from typing import Mapping, Any, NewType, Union

T = NewType('~T', str)


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
