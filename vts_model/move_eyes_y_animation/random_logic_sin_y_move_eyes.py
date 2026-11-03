import random, asyncio

from . import config_eye_y
from pystyle import Colors, Write


async def sin_y_random_logic(delay):

    config_eye_y.random_num_for_move_eye_sin_y = random.uniform(0, 1)
    config_eye_y.gradus_for_blink = random.uniform(-90, 90)


    if config_eye_y.random_num_for_move_eye_sin_y <= config_eye_y.chance:
        config_eye_y.gradus += config_eye_y.gradus_for_blink

        # Write.Print(f'\nsin_y_random_logic\nmoved on: {config_eye_y.gradus_for_blink:.2f} | chance: {config_eye_y.chance:.2f} | random_number: {config_eye_y.random_num_for_move_eye_sin_y:.2f} | tries: {config_eye_y.just_number:.2f}\n\n', Colors.green, interval = 0)
        config_eye_y.chance = 0
        config_eye_y.just_number = 0

    else:
        config_eye_y.just_number += 1
        config_eye_y.chance += config_eye_y.delta

    await asyncio.sleep(delay)