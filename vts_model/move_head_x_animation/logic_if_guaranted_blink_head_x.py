import random, asyncio, math
from .. import move
from pystyle import Colors, Write

from . import config_move_head_x


async def random_timer_for_blink_head_x():

    while True:

        if config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x == True or config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x == True:
            await asyncio.sleep(0.1)
            continue

        config_move_head_x.just_number_for_head_x = random.uniform(0, 1)

        await asyncio.sleep(0.5)

        if config_move_head_x.just_number_for_head_x <= config_move_head_x.chance:
            config_move_head_x.chance = 0
            config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x = True
        else:
            config_move_head_x.chance += config_move_head_x.delta
            # print(f'chance: {config_move_head_x.chance}')


async def blink_for_head_cos_x():

    config_move_head_x.random_gradus_for_head_x = random.uniform(-180, 180)
    config_move_head_x.interval_head_x = 0.08

    if config_move_head_x.random_gradus_for_head_x > config_move_head_x.gradus:
        config_move_head_x.t_rand_speed_for_head_x = abs(config_move_head_x.t_rand_speed_for_head_x)
    
    elif config_move_head_x.random_gradus_for_head_x < config_move_head_x.gradus:
        config_move_head_x.t_rand_speed_for_head_x = -abs(config_move_head_x.t_rand_speed_for_head_x)
    
    else:
        config_move_head_x.interval_head_x = 0.15
        config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x = False

    while True:

        if config_move_head_x.t_rand_speed_for_head_x > 0 and config_move_head_x.gradus >= config_move_head_x.random_gradus_for_head_x:
            break

        elif config_move_head_x.t_rand_speed_for_head_x < 0 and config_move_head_x.gradus <= config_move_head_x.random_gradus_for_head_x:
            break

        config_move_head_x.gradus += config_move_head_x.t_rand_speed_for_head_x
        config_move_head_x.corner = config_move_head_x.gradus * (math.pi / 180)
        config_move_head_x.cos_head_x = math.cos(config_move_head_x.corner) * config_move_head_x.radius

        await asyncio.sleep(config_move_head_x.interval_head_x)

    config_move_head_x.corner = config_move_head_x.gradus * (math.pi / 180)
    config_move_head_x.cos_head_x = math.cos(config_move_head_x.corner) * config_move_head_x.radius

    config_move_head_x.interval_head_x = 0.15
    config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x = False


async def logic_if_guaranted_blink_head_x():
    
    while True:
        
        if config_move_head_x.boolean_for_random_timer_for_blink_head_cos_x == True:
            
            # Write.Print(f'\n\n\nstarted | random_gradus_head_X: {config_move_head_x.random_gradus_for_head_x}\n\n\n', Colors.green_to_blue, interval = 0)
            await blink_for_head_cos_x()
            # Write.Print('\n\n\nended\n\n\n', Colors.purple, interval = 0)

        await asyncio.sleep(0.01)


async def head_x_logs(vts):

    while True:
        
        await asyncio.sleep(config_move_head_x.interval_head_x)
        # Write.Print(f'\n\nhead_x_move\cos_x\nhead_x_cos: {config_move_head_x.cos_head_x:.2f} | gradus: {config_move_head_x.gradus:.2f} | interval: {config_move_head_x.interval_head_x} \n| chance_blink_gradus: {config_move_head_x.chance} | random_gradus: {config_move_head_x.random_gradus_for_head_x}\n\n', Colors.blue, interval = 0)
        await move.head_x_move_animate(vts, config_move_head_x.cos_head_x)


async def blink_for_head_cos_x_start():

    await asyncio.gather(

        random_timer_for_blink_head_x(),
        logic_if_guaranted_blink_head_x()
    )