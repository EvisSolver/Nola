# blink_main.py - ПРАВИЛЬНО
import asyncio, sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from . import logic_if_guaranted_blink_eyes


async def blink_loop(vts):
    """Отдельная функция для основного цикла"""
    
    while True:
        await logic_if_guaranted_blink_eyes.logic_if_guaranted_blink_eyes(vts)


async def blink_main(vts):

    await asyncio.gather(
        logic_if_guaranted_blink_eyes.random_timer(),
        blink_loop(vts)
    )