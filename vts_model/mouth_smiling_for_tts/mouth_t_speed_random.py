import asyncio, random

from . import config_mouth


async def mouth_t_speed_random():

    while True:
        config_mouth.mouth_t_speed_gradus = random.uniform(0, 2)
        await asyncio.sleep(0.1)