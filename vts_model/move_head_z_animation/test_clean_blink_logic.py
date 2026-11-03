import asyncio
import random
import math
import config_move_head_z

async def main():
    
    while True:

        config_move_head_z.corner_sin_z = config_move_head_z.gradus_sin_z * (math.pi / 180)

        config_move_head_z.sin_z = math.sin(config_move_head_z.corner_sin_z) * config_move_head_z.radius_for_sin_z

        config_move_head_z.gradus_sin_z += config_move_head_z.t_speed_for_head_sin_z

        config_move_head_z.boolean_number_for_clean_blink_timer = True
        config_move_head_z.random_number_for_clean_blink_timer = random.uniform(0, 1)
        config_move_head_z.gradus_sin_z_for_clean = random.uniform(-90, 90)
        # bool = True
        await asyncio.sleep(0.2)
        if config_move_head_z.random_number_for_clean_blink_timer <= 0.2:
            # bool = False
            await asyncio.sleep(0.05)
            print('clean blink_animation')

            '''
            
            50

            '''
            if config_move_head_z.gradus_sin_z_for_clean <= config_move_head_z.gradus_sin_z:
                config_move_head_z.gradus_sin_z += config_move_head_z.t_speed_for_head_sin_z
                
                if config_move_head_z.gradus_sin_z >= config_move_head_z.gradus_sin_z_for_clean:
                    config_move_head_z.result_for_move = (config_move_head_z.gradus_sin_z_for_clean - config_move_head_z.gradus_sin_z)
                    config_move_head_z.gradus_sin_z = (config_move_head_z.result_for_move + config_move_head_z.gradus_sin_z)
                    # bool = False

        print(f'sin_z: {config_move_head_z.sin_z} | gradus: {config_move_head_z.gradus_sin_z}')

asyncio.run(main())