import asyncio

from .authentication import authentication

from .move_eyes_x_animation import move_eyes_main_x
from .move_eyes_y_animation import move_eyes_main_y

from .blink_eye_animation import blink_main

from .move_head_x_animation import head_x_main
from .move_head_y_animation import head_y_main
from .move_head_z_animation import head_z_main

from .mouth_smiling_for_tts import mouth_start
from .mouth_puff import mouth_puff_main

async def vts_main(vts):

    await asyncio.gather(

    blink_main.blink_main(vts),
    move_eyes_main_x.move_eyes_main(vts),
    move_eyes_main_y.move_eyes_sin_y_main(vts),
    head_x_main.move_head_x_main(vts),
    head_y_main.head_sin_y_main(vts),
    head_z_main.head_z_main(vts),

    mouth_puff_main.mouth_puff_main(vts),
    mouth_start.main_mouth(vts)

    )