#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """method that takes 2 args and return a tuple"""
    v *= v
    return (k, v)
