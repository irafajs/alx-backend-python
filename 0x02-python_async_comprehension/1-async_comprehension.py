#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import random
from typing import Generator, List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random number from async_gen and return 10 rundom num"""
    return [i async for i in async_generator()]
