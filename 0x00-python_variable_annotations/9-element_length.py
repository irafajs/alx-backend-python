#!/usr/bin/env python3
"""
Shebang to create a PY code
"""


from typing import Sequence, Tuple, List


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    """accept sequence args and return List, Tupe"""
    return [(item, len(item)) for item in lst]
