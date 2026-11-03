import random, asyncio

from . import config_eye_y


async def change_sign_sin_y(delay):

    config_eye_y.random_num_for_eye_sin_y = random.uniform(0, 1)

    if config_eye_y.random_num_for_eye_sin_y <= config_eye_y.chance_for_sign:
        config_eye_y.rand_t_speed_for_eye_sin_y *= -1

        # print(f'change_sign_sin_y\nchanged sign | chance: {config_eye_y.chance_for_sign:.2f} | random_number: {config_eye_y.random_num_for_eye_sin_y:.2f} | tries: {config_eye_y.just_number_for_sign:.2f}\n\n')
        config_eye_y.chance_for_sign = 0
        config_eye_y.just_number_for_sign = 0

    else:
        config_eye_y.just_number_for_sign += 1
        config_eye_y.chance_for_sign += config_eye_y.delta_for_sign

    await asyncio.sleep(delay)