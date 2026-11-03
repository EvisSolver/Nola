import asyncio, random

from . import config_blink, clean_blink_eyes
from pystyle import Colors, Write

async def random_timer():

    while True:

        if config_blink.boolean_for_balance == True:
            await asyncio.sleep(0.1)
            continue

        config_blink.random_number_for_random_timer = random.uniform(0, 1)

        await asyncio.sleep(0.5)

        if config_blink.random_number_for_random_timer <= config_blink.chance_for_random_timer:
            config_blink.booelan_for_random_timer = True
        
        else:
            config_blink.chance_for_random_timer += config_blink.delta_for_random_timer
            # print(f'\n chance: {config_blink.chance_for_random_timer:.2f}')


async def logic_if_guaranted_blink_eyes(vts):

    await asyncio.sleep(0.01)

    if config_blink.booelan_for_random_timer == True:

        # Write.Print(f'\nblinking\n\n', Colors.yellow, interval = 0)
        config_blink.booelan_for_random_timer = False
        
        config_blink.boolean_for_balance = True
        config_blink.chance_for_random_timer = -0.03
        await clean_blink_eyes.clean_blink_eyes(vts)
        config_blink.boolean_for_balance = False