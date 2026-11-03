import asyncio

from . import chance_sign_move_head_y, head_y_move, logic_if_guaranted_blink_head_y

async def head_sin_y_main(vts):
    
    await asyncio.gather(

    head_y_move.sin_y_head(),
    chance_sign_move_head_y.change_sign_for_move_head_sin_y_main(),
    logic_if_guaranted_blink_head_y.blink_for_head_sin_y_start(),
    logic_if_guaranted_blink_head_y.head_y_logs(vts)
    )