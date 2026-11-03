import asyncio, math, random

from . import mouth_puff_config

from vts_model import move

async def mouth_puff_timer_for_random():

    while True:
        mouth_puff_config.mouth_puff_random_number = random.uniform(0, 1)

        if mouth_puff_config.mouth_puff_chance >= mouth_puff_config.mouth_puff_random_number:

            mouth_puff_config.mouth_puff_t_speed *= -1
            mouth_puff_config.mouth_puff_chance = 0.15
            
            if mouth_puff_config.mouth_puff_gradus < 0:
                mouth_puff_config.mouth_puff_gradus = 10
            elif mouth_puff_config.mouth_puff_gradus > 86:
                mouth_puff_config.mouth_puff_gradus = 75

        else: mouth_puff_config.mouth_puff_chance += mouth_puff_config.mouth_puff_delta
        await asyncio.sleep(0.5)

async def mouth_puff_count_and_response(vts):

    while True:
        
        if mouth_puff_config.mouth_puff_gradus > 88 or mouth_puff_config.mouth_puff_gradus < 0:
            mouth_puff_config.mouth_puff_t_speed *= -1

        mouth_puff_config.mouth_puff_gradus += mouth_puff_config.mouth_puff_t_speed

        mouth_puff_config.mouth_puff_corner = mouth_puff_config.mouth_puff_gradus * (math.pi / 180)
        mouth_puff_config.mouth_puff_sin = math.sin(mouth_puff_config.mouth_puff_corner) * mouth_puff_config.mouth_puff_radius
        
        # print(mouth_puff_config.mouth_puff_sin, mouth_puff_config.mouth_puff_gradus)
        await move.mouth_puff(vts, mouth_puff_config.mouth_puff_sin)
        await asyncio.sleep(0.15)


async def mouth_puff_main(vts):
    await asyncio.gather(

        mouth_puff_timer_for_random(),
        mouth_puff_count_and_response(vts)
    )