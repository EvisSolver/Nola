import random, asyncio, math
from pystyle import Colors, Write

async def test():

    delta = 0.01

    chance: float = 0

    guarant_counter = 0

    chance_bool = True

    while True:
        
        n = random.uniform(0, 1)
    
        if n <= chance:
            
            Write.Print(f'\nchance: {chance:.2f} | random_number: {n:.2f}\n\n', Colors.blue_to_black, interval = 0)
            chance = 0
            guarant_counter = 0
            chance_bool = True
        else:
            
            guarant_counter += 1
            if guarant_counter >= 10:
                chance_bool = False
                Write.Print(f'it reach to: {guarant_counter} tries\n', Colors.red, interval = 0)
            chance += delta

            if chance_bool == True:
                print(f'chance: {chance:.2f}')
                chance_bool = True

        await asyncio.sleep(0.1)
