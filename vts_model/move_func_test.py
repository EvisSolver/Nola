import asyncio
import pyvts
import send
import authentication
from api_parameters import PLUGIN_INFO, VTS_API_INFO
from blink_eye_animation import config_blink
from blink_eye_animation import clean_blink_eyes
import math

async def blink_eye(vts):
    # Вычисляем анимацию
    await clean_blink_eyes.clean_blink_eyes()
    
    # Отправляем каждый кадр вручную
    for gradus in range(90, -1, -2):  # от 90 до 0
        corner = gradus * (math.pi / 180)
        sin_y = math.sin(corner) * 1.5
        
        await send.send(vts, {
            'EyeOpenLeft': 1.5 - sin_y,
            'EyeOpenRight': 1.5 - sin_y 
        })
        await asyncio.sleep(0.05)


async def main():
    # Создаём VTS с твоими параметрами
    vts = await authentication.authentication()
    
    # Моргаем
    await blink_eye(vts)
    
    # Закрываем соединение
    await vts.close()


asyncio.run(main())