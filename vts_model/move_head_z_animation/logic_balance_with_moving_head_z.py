import random

import config_move_head_z


async def logic_balance_with_moving_head_z():

    if config_move_head_z.gradus_sin_z >= random.uniform(85.99, 90):
        config_move_head_z.gradus_sin_z = 90

    elif config_move_head_z.gradus_sin_z <= random.uniform(-85.99, -90):
        config_move_head_z.gradus_sin_z = -90

    elif random.uniform(-4, 0) <= config_move_head_z.gradus_sin_z <= random.uniform(0, 4):
        config_move_head_z.gradus_sin_z = 0