#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import random
import asyncio
from typing import List

basic = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """method to return a list of all delays"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_tasks, _ = await asyncio.wait(tasks)
    delays = [task.result() for task in completed_tasks]
    return delays

async def main():
    delay = await wait_n(n, max_delay)

asyncio.run(main())

