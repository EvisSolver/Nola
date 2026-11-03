import asyncio, random, math

from . import config_mouth
from .. import move


async def mouth_start(vts):
    while True:
        if config_mouth.mouth_start_bool:

            # reset after sentence'S
            config_mouth.mouth_start_bool = False
            config_mouth.mouth_close_bool = False
            config_mouth.mouth_gradus = 0
            config_mouth.mouth_t_speed_gradus = 2
            config_mouth.mouth_chance = 0.15

            # 1. ОТКРЫТЬ до 90
            while config_mouth.mouth_gradus < 90:
                config_mouth.mouth_gradus += config_mouth.mouth_t_speed_gradus

                # твой старый расчёт
                config_mouth.mouth_sin_corner = config_mouth.mouth_gradus * (math.pi / 180)
                config_mouth.mouth_sin = math.sin(config_mouth.mouth_sin_corner) * config_mouth.mouth_radius

                await move.mouth_smile(vts, config_mouth.mouth_sin)
                await asyncio.sleep(0.02)

            # 2. hold when tts is talking
            while not config_mouth.mouth_close_bool:
                if random.random() < config_mouth.mouth_chance:  # живость
                    config_mouth.mouth_gradus = random.uniform(20, 90)

                config_mouth.mouth_sin_corner = config_mouth.mouth_gradus * (math.pi / 180)
                config_mouth.mouth_sin = math.sin(config_mouth.mouth_sin_corner) * config_mouth.mouth_radius

                await move.mouth_smile(vts, config_mouth.mouth_sin)
                await asyncio.sleep(0.05)

            # 3. close to 0
            while config_mouth.mouth_gradus > 0:
                config_mouth.mouth_gradus -= config_mouth.mouth_t_speed_gradus
                if config_mouth.mouth_gradus < 0:
                    config_mouth.mouth_gradus = 0

                config_mouth.mouth_sin_corner = config_mouth.mouth_gradus * (math.pi / 180)
                config_mouth.mouth_sin = math.sin(config_mouth.mouth_sin_corner) * config_mouth.mouth_radius

                await move.mouth_smile(vts, config_mouth.mouth_sin)
                await asyncio.sleep(0.02)

        await asyncio.sleep(0.02)


async def main_mouth(vts):
    await mouth_start(vts)