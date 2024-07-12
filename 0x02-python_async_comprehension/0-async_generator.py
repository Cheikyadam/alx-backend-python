#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator():
    """yielding float"""
    for i in range(11):
        await asyncio.sleep(1)
        yield (random.uniform(0, 10))
