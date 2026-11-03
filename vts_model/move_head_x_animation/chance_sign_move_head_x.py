# change_sign_main.py
import asyncio, random

from pystyle import Colors, Write

from . import config_move_head_x


async def sign_timer_for_head_x():

    while True:

        if config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x == True or config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x == True:

            await asyncio.sleep(0.1)
            continue
        
        else:
            config_move_head_x.random_number_for_random_timer_for_sign_cos_x = random.uniform(0, 1)

            await asyncio.sleep(0.5)

            if config_move_head_x.random_number_for_random_timer_for_sign_cos_x <= config_move_head_x.chance_for_sign:
                # Write.Print(f'\nchanged sign\n', Colors.green, interval = 0)
                config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x = True

                config_move_head_x.chance_for_sign = 0

            else:
                config_move_head_x.chance_for_sign += config_move_head_x.delta_for_sign


async def change_sign_head_cos_x():

    while True:
        
        await asyncio.sleep(0.024999)

        if config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x == True:
            
            config_move_head_x.t_rand_speed_for_head_x *= -1

            config_move_head_x.t_rand_speed_for_head_x = random.uniform(2, 4)

            config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x = False


async def change_sign_main_for_move_head_cos_x_main():

    await asyncio.gather(

        sign_timer_for_head_x(),
        change_sign_head_cos_x()
    )