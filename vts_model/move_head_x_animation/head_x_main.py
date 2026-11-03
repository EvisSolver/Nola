import asyncio

from . import head_x_move, chance_sign_move_head_x, logic_if_guaranted_blink_head_x


async def move_head_x_main(vts):

    await asyncio.gather(

        head_x_move.cos_x_head(),
        chance_sign_move_head_x.change_sign_main_for_move_head_cos_x_main(),
        logic_if_guaranted_blink_head_x.blink_for_head_cos_x_start(),
        logic_if_guaranted_blink_head_x.head_x_logs(vts)
    )