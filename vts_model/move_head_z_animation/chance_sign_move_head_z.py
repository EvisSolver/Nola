import asyncio, random

from . import config_move_head_z


async def sign_timer_for_head_z():

    while True:

        if config_move_head_z.boolean_for_sign_timer == True:
            asyncio.sleep(0.1)
            continue

        else:
            config_move_head_z.random_number_for_sign_timer = random.uniform(0, 1)
        
            await asyncio.sleep(0.5)

            if config_move_head_z.random_number_for_sign_timer <= config_move_head_z.chance_for_sign:

                config_move_head_z.boolean_for_sign_timer == True
                config_move_head_z.chance_for_sign = 0

            else:
                config_move_head_z.chance_for_sign += config_move_head_z.delta_for_sign


async def change_sign_for_head_z():

    while True:

        await asyncio.sleep(0.02499)

        if config_move_head_z.boolean_for_sign_timer == True:
            
            config_move_head_z.t_speed_for_head_sin_z *= -1


async def change_sign_for_head_z_start():

    await asyncio.gather(

        sign_timer_for_head_z(),
        change_sign_for_head_z()
    )