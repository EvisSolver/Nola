import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


import asyncio, math, random
from . import config_eye_y, logic_if_move_eyes_sin_y, sin_y_changing_sign_move_eyes, random_logic_sin_y_move_eyes 
from .. import move

from pystyle import Colors, Write


async def sin_y(vts, delay):
    
    config_eye_y.radius = random.uniform(0.5, 1)
    config_eye_y.gradus += config_eye_y.rand_t_speed_for_eye_sin_y
    config_eye_y.corner = config_eye_y.gradus * (math.pi / 180)
    config_eye_y.sin_y_value = math.sin(config_eye_y.corner) * config_eye_y.radius

    config_eye_y.gradus = round(config_eye_y.gradus, 2)
    config_eye_y.sin_y_value = round(config_eye_y.sin_y_value, 2)

    # Write.Print(f'\nsin: {config_eye_y.sin_y_value} | gradus: {config_eye_y.gradus}\n', Colors.purple, interval = 0)


    await logic_if_move_eyes_sin_y.sin_y_logic(0.2),
    await sin_y_changing_sign_move_eyes.change_sign_sin_y(0.1),
    await random_logic_sin_y_move_eyes.sin_y_random_logic(0.1)


    await move.eye_y_move_animate(vts, config_eye_y.sin_y_value)

    await asyncio.sleep(delay)
