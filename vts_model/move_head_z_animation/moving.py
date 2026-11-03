import math, asyncio

from . import config_move_head_z, logic_when_moving_head_z


async def moving():

    while True:

        await asyncio.sleep(config_move_head_z.interval)

        await logic_when_moving_head_z.logic_when_moving_head_z()
        
        config_move_head_z.gradus_sin_z += config_move_head_z.t_speed_for_head_sin_z
        
        config_move_head_z.corner_sin_z = config_move_head_z.gradus_sin_z * (math.pi / 180)
        config_move_head_z.sin_for_z = math.sin(config_move_head_z.corner_sin_z) * config_move_head_z.radius_for_sin_z