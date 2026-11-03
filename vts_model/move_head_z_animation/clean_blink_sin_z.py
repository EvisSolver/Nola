import asyncio, random, math

from . import config_move_head_z


from vts_model import move


async def random_timer_for_head_z():

    while True:

        if config_move_head_z.boolean_number_for_timer_random_number == True:
            await asyncio.sleep(0.1)
            continue


        config_move_head_z.random_number_for_clean_blink_timer = random.uniform(0, 1)
        
        await asyncio.sleep(0.5)

        if config_move_head_z.random_number_for_clean_blink_timer <= config_move_head_z.chance_for_clean_blink_timer:
                config_move_head_z.boolean_number_for_timer_random_number = True
                # print('prok')
                config_move_head_z.chance_for_clean_blink_timer = 0
        else:
            config_move_head_z.chance_for_clean_blink_timer += config_move_head_z.delta_for_clean_blink_timer


async def moving_for_blink():
    # print('flksadl\n\n\n')

    config_move_head_z.random_gradus_sin_z_for_clean = random.uniform(-90, 90)
    config_move_head_z.interval = 0.05

    if config_move_head_z.random_gradus_sin_z_for_clean > config_move_head_z.gradus_sin_z:
        config_move_head_z.t_speed_for_head_sin_z = abs(config_move_head_z.t_speed_for_head_sin_z)

    elif config_move_head_z.random_gradus_sin_z_for_clean < config_move_head_z.gradus_sin_z:
        config_move_head_z.t_speed_for_head_sin_z = -abs(config_move_head_z.t_speed_for_head_sin_z)

    else:
        config_move_head_z.interval = 0.2
        config_move_head_z.boolean_number_for_timer_random_number = False


    while True:

        if config_move_head_z.t_speed_for_head_sin_z > 0 and config_move_head_z.gradus_sin_z >= config_move_head_z.random_gradus_sin_z_for_clean:
            config_move_head_z.gradus_sin_z = config_move_head_z.random_gradus_sin_z_for_clean
            break

        elif config_move_head_z.t_speed_for_head_sin_z < 0 and config_move_head_z.gradus_sin_z <= config_move_head_z.random_gradus_sin_z_for_clean:
            config_move_head_z.gradus_sin_z = config_move_head_z.random_gradus_sin_z_for_clean
            break

        config_move_head_z.gradus_sin_z += config_move_head_z.t_speed_for_head_sin_z
        config_move_head_z.corner_sin_z = config_move_head_z.gradus_sin_z * (math.pi / 180)
        config_move_head_z.sin_for_z = math.sin(config_move_head_z.corner_sin_z) * config_move_head_z.radius_for_sin_z

        await asyncio.sleep(config_move_head_z.interval)

    config_move_head_z.corner_sin_z = config_move_head_z.gradus_sin_z * (math.pi / 180)
    config_move_head_z.sin_for_z = math.sin(config_move_head_z.corner_sin_z) * config_move_head_z.radius_for_sin_z

    config_move_head_z.interval = 0.2
    config_move_head_z.boolean_number_for_timer_random_number = False


async def logic_if_guaranted_blink_head_z():

    while True:

        if config_move_head_z.boolean_number_for_timer_random_number == True:
            
            # print('blinking...\n\n\n')
            await moving_for_blink()

        await asyncio.sleep(0.01)

        
async def logs(vts):

    while True:

        await asyncio.sleep(config_move_head_z.interval)
        # print(f'sin_z: {config_move_head_z.sin_for_z} | gradus: {config_move_head_z.gradus_sin_z:.2f} | chance: {config_move_head_z.chance_for_clean_blink_timer:.2f} | random_num: {config_move_head_z.random_number_for_clean_blink_timer:.2f} | {config_move_head_z.random_gradus_sin_z_for_clean} | bool: {config_move_head_z.boolean_number_for_timer_random_number} | interval: {config_move_head_z.interval:.2f}')
        await move.head_z_move_animate(vts, config_move_head_z.sin_for_z)


async def start_gather():

    await asyncio.gather(

        random_timer_for_head_z(),
        logic_if_guaranted_blink_head_z()
    )