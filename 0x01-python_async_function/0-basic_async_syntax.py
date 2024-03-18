#!/usr/bin/env python3
"""
Shebang to create a PY script
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Method to generate random number betweeb 0-10"""
    rand_num = random.uniform(0, max_delay)
    #rand_num = random.random() * max_delay
    await asyncio.sleep(rand_num)
    return rand_num
