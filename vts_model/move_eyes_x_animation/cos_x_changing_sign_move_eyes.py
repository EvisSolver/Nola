import asyncio, random

from . import config_eye_x

from pystyle import Colors, Write


async def change_sign():

    config_eye_x.random_num_for_eye_cos_x = random.uniform(0, 1)

    await asyncio.sleep(0.3)

    if config_eye_x.random_num_for_eye_cos_x <= config_eye_x.chance_for_sign:
        config_eye_x.rand_t_speed_for_eye_cos_x *= -1
        
        # Write.Print(f'\nchange_sign\nchance: {config_eye_x.chance_for_sign:.2f} | random_number: {config_eye_x.random_num_for_eye_cos_x:.2f}\n\n', Colors.purple_to_blue, interval = 0)
        
        config_eye_x.chance_for_sign = 0
        config_eye_x.just_number_for_sign = 0

    else:
        config_eye_x.chance_for_sign += config_eye_x.delta_for_sign