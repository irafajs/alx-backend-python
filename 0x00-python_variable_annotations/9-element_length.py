#!/usr/bin/env python3
"""
Shebang to create a PY code
"""


from typing import Sequence, Tuple, List, Iterable


ret_lst = Iterable[Sequence]

def element_length(lst: ret_lst) -> List[Tuple[Sequence, int]]:
    """accept sequence args and return List, Tupe"""
    return [(item, len(item)) for item in lst]
