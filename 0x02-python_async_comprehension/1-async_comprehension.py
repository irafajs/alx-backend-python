#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import random
from typing import Generator


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """Collect 10 random number from async_gen and return 10 rundom num"""
    async_gen: Generator[float, None, None] = async_generator()
    return [i async for i in async_gen]
