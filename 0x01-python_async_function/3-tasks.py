#!/usr/bin/env python3
"""
Shebang to create a PY script
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function that return an asyncio task in python"""
    return asyncio.create_task(wait_random(max_delay))
