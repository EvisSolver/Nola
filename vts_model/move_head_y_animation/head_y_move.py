import asyncio, math

from . import config_move_head_y, logic_when_moving_head_y


async def sin_y_head():
    
    while True:

        await asyncio.sleep(config_move_head_y.interval_head_y)
        await logic_when_moving_head_y.when_moving_head_y()

        config_move_head_y.gradus += config_move_head_y.t_speed_head_y

        config_move_head_y.corner = config_move_head_y.gradus * (math.pi / 180)
        config_move_head_y.sin_head_y = math.sin(config_move_head_y.corner) * config_move_head_y.radius
        
        # print(f'\nsin_y: {config_move_head_y.sin_head_y:.2f} | gradus: {config_move_head_y.gradus:.2f} | t_speed: {config_move_head_y.t_speed_head_y:.2f} | radius: {config_move_head_y.radius:.2f}\n\n')
