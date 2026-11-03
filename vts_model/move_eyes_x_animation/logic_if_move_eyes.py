import random

from . import config_eye_x


async def cos_x_logic():

    if config_eye_x.gradus >= 90 or config_eye_x.gradus <= -90:
        config_eye_x.rand_t_speed_for_eye_cos_x = -config_eye_x.rand_t_speed_for_eye_cos_x

        if config_eye_x.gradus >= random.uniform(86.99, 90):
            config_eye_x.gradus = 90

        elif config_eye_x.gradus <= random.uniform(-86.99, -90):
            config_eye_x.gradus = -90