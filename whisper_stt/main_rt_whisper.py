from . import if_start_logic

from . import transcribition


async def whisper_main():

    await if_start_logic.if_start_logic()
    text = await transcribition.transcribe()

    return text