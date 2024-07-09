#!/usr/bin/env python3
"""simple async func"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
