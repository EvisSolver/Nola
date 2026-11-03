import random, asyncio

from . import config_eye_y


async def sin_y_logic(delay):

    if config_eye_y.gradus >= 90 or config_eye_y.gradus <= -90:
            config_eye_y.rand_t_speed_for_eye_sin_y = -config_eye_y.rand_t_speed_for_eye_sin_y
            
            if config_eye_y.gradus >= random.uniform(86.99, 90):
                config_eye_y.gradus = 90
            
            elif config_eye_y.gradus <= random.uniform(-86.99, -90):
                config_eye_y.gradus = -90

    await asyncio.sleep(delay)