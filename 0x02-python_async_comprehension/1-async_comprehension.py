#!/usr/bin/env python3
"""async comprehension"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> None:
    """the function def"""
    return [number async for number in async_generator()]
