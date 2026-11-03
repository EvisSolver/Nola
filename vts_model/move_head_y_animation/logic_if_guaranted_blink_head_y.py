import asyncio, random, math

from pystyle import Colors, Write

from . import config_move_head_y
from .. import move


async def timer_for_blink_head_sin_y():

    while True:

        if config_move_head_y.boolean_for_timer_blink_head_y == True or config_move_head_y.boolean_for_timer_sign_move_head_y == True:
            await asyncio.sleep(0.1)
            continue

        config_move_head_y.random_number_for_blink_sin_head_y = random.uniform(0, 1)
        
        await asyncio.sleep(0.5)

        if config_move_head_y.random_number_for_blink_sin_head_y <= config_move_head_y.chance_for_blink:
                config_move_head_y.chance_for_blink = 0
                config_move_head_y.boolean_for_timer_blink_head_y = True

        else:
            config_move_head_y.chance_for_blink += config_move_head_y.delta_for_blink


async def blink_for_head_sin_y():
     
    config_move_head_y.random_gradus_for_head_y = random.uniform(-90, 90)
    # Write.Print(f'\n\n\nstarted | random_gradus_head_y: {config_move_head_y.random_gradus_for_head_y}\n\n\n', Colors.purple, interval = 0)
    config_move_head_y.interval_head_y = 0.04
     
    if config_move_head_y.random_gradus_for_head_y > config_move_head_y.gradus:
        config_move_head_y.t_speed_head_y = abs(config_move_head_y.t_speed_head_y)
    
    elif config_move_head_y.random_gradus_for_head_y < config_move_head_y.gradus:
        config_move_head_y.t_speed_head_y = -abs(config_move_head_y.t_speed_head_y)

    else:
        config_move_head_y.interval_head_y = 0.1
        config_move_head_y.boolean_for_timer_blink_head_y = False

    while True:

        if config_move_head_y.t_speed_head_y > 0 and config_move_head_y.gradus >= config_move_head_y.random_gradus_for_head_y:
            break

        elif config_move_head_y.t_speed_head_y < 0 and config_move_head_y.gradus <= config_move_head_y.random_gradus_for_head_y:
            break

        config_move_head_y.gradus += config_move_head_y.t_speed_head_y
        config_move_head_y.corner = config_move_head_y.gradus * (math.pi / 180)
        config_move_head_y.sin_head_y = math.sin(config_move_head_y.corner) * config_move_head_y.radius

        await asyncio.sleep(config_move_head_y.interval_head_y)

    config_move_head_y.corner = config_move_head_y.gradus * (math.pi / 180)
    config_move_head_y.sin_head_y = math.sin(config_move_head_y.corner) * config_move_head_y.radius

    config_move_head_y.interval_head_y = 0.1
    config_move_head_y.boolean_for_timer_blink_head_y = False


async def logic_if_guaranted_blink_head_x():

    while True:

        if config_move_head_y.boolean_for_timer_blink_head_y == True:

            await blink_for_head_sin_y()
            # Write.Print('\n\n\nended\n\n\n', Colors.purple, interval = 0)

        await asyncio.sleep(0.01)
        

async def head_y_logs(vts):

    while True:

        await asyncio.sleep(config_move_head_y.interval_head_y)
        # Write.Print(f'\n\nhead_y_logs:\nrandom_radius: {config_move_head_y.radius}\nhead_y_sin: {config_move_head_y.sin_head_y} | head_y_gradus: {config_move_head_y.gradus} | chance_for_blink: {config_move_head_y.chance_for_blink} | random_gradus_for_blink: {config_move_head_y.random_gradus_for_head_y}\ninterval: {config_move_head_y.interval_head_y} | radius: {config_move_head_y.radius}', Colors.red_to_white, interval = 0)
        await move.head_y_move_animate(vts, config_move_head_y.sin_head_y)


async def blink_for_head_sin_y_start():

    await asyncio.gather(

        timer_for_blink_head_sin_y(),
        logic_if_guaranted_blink_head_x()
    )