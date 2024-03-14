#!/usr/bin/env python3
"""
Shebang to create a PY script
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """method accepts arg as float and return callable float"""
    def mul_fun(x: float) -> float:
        return x * multiplier

    return mul_fun
