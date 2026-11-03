import random, asyncio, math

from . import logic_if_blink, config_blink
from move_eyes_x_animation import config_eye_x
from .. import move

from pystyle import Colors, Write


async def clean_blink_eyes(vts):

    delay = 0.02

    while True:
        await logic_if_blink.logic_if()
        config_blink.corner = config_blink.gradus * (math.pi / 180)
        config_blink.sin_y = math.sin(config_blink.corner) * config_blink.radius

            
        # print(f'{config_blink.sin_y:.2f} | {config_blink.gradus:.2f}')
        
        await move.blink_eyes_animate(vts, config_blink.sin_y)

        if config_blink.sin_y >= 1:
            config_eye_x.gradus = random.uniform(-90, 90)
            break


        await asyncio.sleep(delay)