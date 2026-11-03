import sys


async def sys_logic(full_text):

    clean = full_text.strip().lower().rstrip('.,!?')

    if clean == 'закрыть':
        print('exit of the programm..')
        sys.exit(0)