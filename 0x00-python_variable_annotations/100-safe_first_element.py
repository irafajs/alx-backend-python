#!/usr/bin/env python3
"""
Shebang to make a PY script
"""


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """method that doing duck typing"""
    if lst:
        return lst[0]
    else:
        return None
