import random

from . import config_eye_x

from pystyle import Colors, Write


async def cos_x_random_logic():

    config_eye_x.random_num_for_move_eye_cos_x = random.uniform(0, 1)
    config_eye_x.gradus_for_blink = random.uniform(-90, 90)

    if config_eye_x.random_num_for_move_eye_cos_x <= config_eye_x.chance:
        config_eye_x.gradus += random.uniform(-60, 60)
        # Write.Print(f'\ncos_x_random_logic\ngradus change on: {config_eye_x.gradus_for_blink:.2f} | chance: {config_eye_x.chance:.2f} | random_number: {config_eye_x.random_num_for_move_eye_cos_x:.2f}\n\n', Colors.purple, interval = 0)
        config_eye_x.chance = 0
        config_eye_x.just_number = 0

    else:
        config_eye_x.just_number += 1
        config_eye_x.chance += config_eye_x.delta

        # if config_eye_x.just_number >= 10:

        #     Write.Print(f'\ncos_x_random_logic\nchance: {config_eye_x.chance:.2f} | {config_eye_x.just_number} tries\n\n', Colors.purple, interval = 0)