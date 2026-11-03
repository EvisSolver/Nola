import asyncio, math

from . import logic_if_move_head_x, config_move_head_x


async def cos_x_head():

    while True:

        await asyncio.sleep(config_move_head_x.interval_head_x)
        await logic_if_move_head_x.head_cos_x_logic()

        config_move_head_x.gradus += config_move_head_x.t_rand_speed_for_head_x
        
        config_move_head_x.corner = config_move_head_x.gradus * (math.pi / 180)
        config_move_head_x.cos_head_x = math.cos(config_move_head_x.corner) * config_move_head_x.radius

        # print(f'cos_x: {config_move_head_x.cos_head_x} | gradus: {config_move_head_x.gradus} | chance: {config_move_head_x.chance_for_sign} | sign_bool: {config_move_head_x.boolean_for_random_timer_for_sign_head_cos_x}')