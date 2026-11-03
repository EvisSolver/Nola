from . import config_move_head_z


async def logic_when_moving_head_z():

    if config_move_head_z.gradus_sin_z >= 90 or config_move_head_z.gradus_sin_z <= -90:
        config_move_head_z.t_speed_for_head_sin_z *= -1