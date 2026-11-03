import asyncio, random, math, sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import config_move_head_z, logic_when_moving_head_z, logic_balance_with_moving_head_z


async def start():

    while True:

        config_move_head_z.corner_sin_z = config_move_head_z.gradus_sin_z * (math.pi / 180)
        await logic_when_moving_head_z.logic_when_moving_head_z()
        config_move_head_z.sin_z = math.sin(config_move_head_z.corner_sin_z) * config_move_head_z.radius_for_sin_z

        config_move_head_z.gradus_sin_z += config_move_head_z.t_speed_for_head_sin_z

        await logic_balance_with_moving_head_z.logic_balance_with_moving_head_z()

        print(f'sin_z: {config_move_head_z.sin_z} | gradus: {config_move_head_z.gradus_sin_z}')
        await asyncio.sleep(0.2)

asyncio.run(start())