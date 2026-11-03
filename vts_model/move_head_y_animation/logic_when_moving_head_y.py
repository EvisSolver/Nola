from . import config_move_head_y


async def when_moving_head_y():

    if config_move_head_y.gradus >= 90 or config_move_head_y.gradus <= -90:
        config_move_head_y.t_speed_head_y *= -1