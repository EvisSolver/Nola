import asyncio, math

from . import config_eye_x, logic_if_move_eyes, random_logic_cos_x_move_eyes, cos_x_changing_sign_move_eyes

from .. import move


async def cos_x(vts, delay):

    config_eye_x.gradus += config_eye_x.rand_t_speed_for_eye_cos_x

    config_eye_x.corner = config_eye_x.gradus * (math.pi / 90)
    config_eye_x.cos_x_move_eyes = math.cos(config_eye_x.corner) * config_eye_x.radius

    await logic_if_move_eyes.cos_x_logic()
    await random_logic_cos_x_move_eyes.cos_x_random_logic()
    await cos_x_changing_sign_move_eyes.change_sign()

    config_eye_x.cos_x_move_eyes = round(config_eye_x.cos_x_move_eyes, 2)
    config_eye_x.gradus = round(config_eye_x.gradus, 2)

    await move.eye_x_move_animate(vts, config_eye_x.cos_x_move_eyes)
    # print(f'cos_x: {config_eye_x.cos_x_move_eyes} | gradus: {config_eye_x.gradus}') 


    await asyncio.sleep(delay)