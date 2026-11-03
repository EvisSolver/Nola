from . import sin_y_move_eyes

import os, sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


async def move_eyes_sin_y_main(vts):
    
    while True:

        await sin_y_move_eyes.sin_y(vts, 0.05)