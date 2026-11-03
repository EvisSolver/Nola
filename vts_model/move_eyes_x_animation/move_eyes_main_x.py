from . import cos_x_move_eyes


async def move_eyes_main(vts):

    while True:
        await cos_x_move_eyes.cos_x(vts, 0.05)