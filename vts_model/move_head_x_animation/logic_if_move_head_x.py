from . import config_move_head_x


async def head_cos_x_logic():

    if config_move_head_x.gradus >= 180 or config_move_head_x.gradus <= -180:
        config_move_head_x.t_rand_speed_for_head_x *= -1
