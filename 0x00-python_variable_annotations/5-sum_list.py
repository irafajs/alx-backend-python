#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


from typing import List


floatlist = List[float]


def sum_list(input_list: floatlist) -> float:
    """method accept list of float and return sum of float"""
    total_args_sum: float = 0
    for arg in input_list:
        total_args_sum += arg

    return total_args_sum
