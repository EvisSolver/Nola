from .send import send


async def blink_eyes_animate(vts, value):

    await send(
        vts,
        {
            'EyeOpenLeft': value,
            'EyeOpenRight': value
        }
    )


async def eye_x_move_animate(vts, value):

    await send(
        vts,
        {
            'EyeRightX': value,
            'EyeLeftX': value
        }
    )


async def eye_y_move_animate(vts, value):

    await send(
        vts,
        {
            'EyeRightY': value,
            'EyeLeftY': value
        }
    )


async def head_x_move_animate(vts, value):

    await send(
        vts,
        {
            'FaceAngleX': value
        }
    )


async def head_y_move_animate(vts, value):

    await send(
        vts,
        {
            'FaceAngleY': value
        }
    )


async def head_z_move_animate(vts, value):

    await send(
        vts,
        {
            'FaceAngleZ': value
        }
    )


async def mouth_smile(vts, value):
    
    await send(
        vts,
        {
            'MouthSmile': value
        }
    )

async def mouth_puff(vts, value):

    await send(
        vts,
        {
            'CheekPuff': value
        }
    )