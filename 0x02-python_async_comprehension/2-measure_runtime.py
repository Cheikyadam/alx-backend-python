#!/usr/bin/env python3
"""gather async"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> None:
    """measure runtime"""
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(), async_comprehension(),
            async_comprehension(), async_comprehension())
    return time.perf_counter() - start
