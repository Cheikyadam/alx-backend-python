#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator() -> None:
    """yielding float"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
