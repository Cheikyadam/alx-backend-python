#!/usr/bin/env python3
"""multiple coroutines"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """wait random"""

    if n <= 0:
        return []

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    for i in range(len(delays) - 1, 0, -1):
        if delays[i] < delays[i - 1]:
            delays[i], delays[i - 1] = delays[i - 1], delays[i]
        else:
            break

    return delays
