import asyncio

from . import moving, clean_blink_sin_z, chance_sign_move_head_z


async def head_z_main(vts):


        await asyncio.gather(

        moving.moving(),
        chance_sign_move_head_z.change_sign_for_head_z_start(),
        clean_blink_sin_z.start_gather(),
        clean_blink_sin_z.logs(vts)
        )