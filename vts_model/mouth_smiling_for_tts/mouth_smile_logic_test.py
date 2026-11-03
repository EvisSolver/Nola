import asyncio, math, random, time


mouth_start_bool = True

global gradus, t_speed_gradus, radius

gradus = 90
t_speed_gradus = 2

radius = 1


async def t_speed_random():

    while True:
            
        global t_speed_gradus
        t_speed_gradus = random.uniform(0, 2)

        await asyncio.sleep(0.1)

async def mouth_up(): 

    global gradus, t_speed_gradus, radius
    global mouth_start_bool

    while True:

        if gradus <= 0:
            t_speed_gradus *= -1 

        if 2 >= gradus >= -2 or gradus == 0:
            print("mouth_up stopped")
            mouth_start_bool = False
            break

        if mouth_start_bool == True:
            gradus -= t_speed_gradus

            sin_corner = gradus * (math.pi / 180)
            sin = math.sin(sin_corner) * radius

            await asyncio.sleep(0.02)
            print(sin, gradus)


async def mouth_down():

    global gradus, t_speed_gradus, radius
    global mouth_start_bool

    while True:

        if gradus <= -90:
            break

        if mouth_start_bool == False:

            gradus += -t_speed_gradus

            sin_corner = gradus * (math.pi / 180)
            sin = math.sin(sin_corner) * radius
            print(sin, gradus)

        await asyncio.sleep(0.02)


async def start_animation():

    global mouth_start_bool

    randomyzer = asyncio.create_task(t_speed_random())
    
    print("mouth_up bdfgbfdg")
    await mouth_up()

    mouth_start_bool == True
    print("TTS talking...")
    await asyncio.sleep(2)
    # time.sleep(2)

    print("mouth_down started")
    await mouth_down()
    randomyzer.cancel()

asyncio.run(start_animation())