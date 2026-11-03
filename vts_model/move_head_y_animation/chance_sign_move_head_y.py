import random, asyncio

from pystyle import Colors, Write

from . import config_move_head_y


async def timer_for_sign_move_head_y():

    while True:

        if config_move_head_y.boolean_for_timer_sign_move_head_y == True or config_move_head_y.boolean_for_timer_blink_head_y == True:
            await asyncio.sleep(0.1)
            continue

        else:
            config_move_head_y.random_number_for_sign_sin_head_y = random.uniform(0, 1)

            await asyncio.sleep(0.5)

            if config_move_head_y.random_number_for_sign_sin_head_y <= config_move_head_y.chance_for_sign:
                # Write.Print(f'\nchance: {config_move_head_y.chance_for_sign}\n', Colors.green, interval = 0)
                config_move_head_y.boolean_for_timer_sign_move_head_y = True
                config_move_head_y.chance_for_sign = 0

            else:
                config_move_head_y.chance_for_sign += config_move_head_y.delta_for_sign
                # print(f'chance else: {config_move_head_y.chance_for_sign}')


async def change_sign_for_move_head_sin_y():
    
    while True:

        await asyncio.sleep(0.024999)

        if config_move_head_y.boolean_for_timer_sign_move_head_y == True:

            # Write.Print(f'\nsign changed\n', Colors.green, interval = 0)

            config_move_head_y.t_speed_head_y *= -1
            
            config_move_head_y.t_speed_head_y = random.uniform(1, 3)

            config_move_head_y.boolean_for_timer_sign_move_head_y = False


async def change_sign_for_move_head_sin_y_main():

    await asyncio.gather(

        timer_for_sign_move_head_y(),
        change_sign_for_move_head_sin_y()
    )