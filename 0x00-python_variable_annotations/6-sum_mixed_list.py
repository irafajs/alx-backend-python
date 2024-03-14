#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


from typing import List, Union


listmixed = List[Union[int, float]]


def sum_mixed_list(mxd_lst: listmixed) -> float:
    """Method takes list of mixed and return float"""
    sumOfArgs: float = 0
    for args in mxd_lst:
        sumOfArgs += args

    return sumOfArgs
