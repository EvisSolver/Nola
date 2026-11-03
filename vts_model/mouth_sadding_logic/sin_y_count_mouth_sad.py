import math, asyncio

from . import config_mouth_sadding
from .. import move


async def sin_y_mouth_sad(vts):

    config_mouth_sadding.gradus_mouth_smile = 0
    
    while True:

        config_mouth_sadding.gradus_mouth_sad -= config_mouth_sadding.t_speed_mouth_sad
        
        config_mouth_sadding.corner_mouth_sad = config_mouth_sadding.gradus_mouth_sad * (math.pi / 180)
        config_mouth_sadding.sin_y_mouth_sad = math.sin(config_mouth_sadding.corner_mouth_sad) * 1
        
        await move.mouth_smile(vts, config_mouth_sadding.sin_y_mouth_sad)

        if config_mouth_sadding.gradus_mouth_sad == -90:
            await asyncio.sleep(2)

        if config_mouth_sadding.gradus_mouth_sad <= -176:
            config_mouth_sadding.gradus_mouth_sad = -179.99
            break

        await asyncio.sleep(0.05)