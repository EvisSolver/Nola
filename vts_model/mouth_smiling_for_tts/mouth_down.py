import asyncio, math

from . import config_mouth

from .. import move


async def mouth_down(vts):
    
    print("mouth_down started")
    while True:

        if config_mouth.mouth_gradus <= 0.01:
            config_mouth.mouth_close_bool = False
            break

        elif config_mouth.mouth_close_bool == True:
            config_mouth.mouth_gradus -= config_mouth.mouth_t_speed_gradus

            config_mouth.mouth_sin_corner = config_mouth.mouth_gradus * (math.pi / 180)
            config_mouth.mouth_sin = math.sin(config_mouth.mouth_sin_corner) * config_mouth.mouth_radius

        await asyncio.sleep(0.02)
        print(config_mouth.mouth_sin, config_mouth.mouth_gradus)

        await move.mouth_smile(vts, config_mouth.mouth_sin)