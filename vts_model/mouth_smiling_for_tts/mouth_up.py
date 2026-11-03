import asyncio, math, random

from . import config_mouth

from vts_model import move


async def mouth_up_timer():

        
    while True:

        if config_mouth.mouth_close_bool == True:
            break

        config_mouth.mouth_up_random_number = random.uniform(0, 1)
        if config_mouth.mouth_up_random_number < config_mouth.mouth_chance:
            config_mouth.mouth_change_sign_up_bool = True
            print("mouth_up change sign")
            config_mouth.mouth_chance = -0.01

        else: config_mouth.mouth_up_random_number += config_mouth.mouth_delta_for_chance

        await asyncio.sleep(0.1)
     
async def mouth_up_change_sign():
    if config_mouth.mouth_change_sign_up_bool == True:
        config_mouth.mouth_t_speed_gradus *= -1      

async def mouth_up(vts):

    print("mouth_up started")
    while True:

        if config_mouth.mouth_close_bool == True:
            print("mouth_up_stopped | mouth_close_started")
            break
            
        if 0 <= config_mouth.mouth_gradus < 90:
            await mouth_up_change_sign()

            config_mouth.mouth_gradus += config_mouth.mouth_t_speed_gradus
            
            config_mouth.mouth_sin_corner = config_mouth.mouth_gradus * (math.pi / 180)
            config_mouth.mouth_sin = math.sin(config_mouth.mouth_sin_corner) * config_mouth.mouth_radius

            print(config_mouth.mouth_sin, config_mouth.mouth_gradus)
        
        else: config_mouth.mouth_t_speed_gradus *= -1
        
        await asyncio.sleep(0.02)


        await move.mouth_smile(vts, config_mouth.mouth_sin)