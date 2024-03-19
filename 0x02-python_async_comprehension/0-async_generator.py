#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine to return a float number"""
    for value in range(10):
        random_num = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield random_num
