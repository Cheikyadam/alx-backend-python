#!/usr/python3
import asyncio
import random
"""simple async func"""


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
