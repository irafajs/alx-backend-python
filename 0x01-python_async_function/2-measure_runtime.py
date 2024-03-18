#!/usr/bin/env python3
"""
Shebang to create a PY code
"""


import random
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """method to return a max time used by wait_n"""
    start_time = time.time()
    delays = asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
