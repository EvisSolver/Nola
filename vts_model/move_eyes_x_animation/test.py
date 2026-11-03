import asyncio, math, random

import config_eye_x
from pystyle import Colors, Write


async def cos_x_eyes_move():

    for i in range(90):

        config_eye_x.gradus += config_eye_x.rand_t_speed_for_eye_cos_x
        corner = config_eye_x.gradus * (math.pi / 90)
        cos_x = math.cos(corner) * config_eye_x.radius

        config_eye_x.random_num_for_eye_cos_x = random.uniform(0, 1)
        config_eye_x.random_num_for_move_eye_cos_x = random.uniform(0, 1)

        if config_eye_x.gradus >= 90 or config_eye_x.gradus <= -90:
            config_eye_x.rand_t_speed_for_eye_cos_x = -config_eye_x.rand_t_speed_for_eye_cos_x

            if config_eye_x.gradus >= random.uniform(86.99, 90):
                config_eye_x.gradus = 90

            elif config_eye_x.gradus <= random.uniform(-86.99, 90):
                config_eye_x.gradus = -90

        if config_eye_x.random_num_for_move_eye_cos_x <= config_eye_x.chance:
            config_eye_x.gradus += random.uniform(-60, 60)
            Write.Print(f'\n+\n\ngradus: {config_eye_x.gradus:.2f} | random_number: {config_eye_x.random_num_for_move_eye_cos_x:.2f} | chance: {config_eye_x.chance:.2f}\n', Colors.red, interval = 0.05)
            config_eye_x.chance = 0

        else:
            config_eye_x.chance += config_eye_x.delta

            Write.Print(f'chance: {config_eye_x.chance:.2f} | random_number: {config_eye_x.random_num_for_move_eye_cos_x:.2f}\n', Colors.purple, interval = 0)
            
        if config_eye_x.random_num_for_eye_cos_x <= 0.2:
            config_eye_x.rand_t_speed_for_eye_cos_x *= -1
            print('\nchanging sign...\n')
        Write.Print(f'cos_x: {cos_x}\n', Colors.green_to_yellow, interval = 0)
        await asyncio.sleep(0.2)
