import asyncio

from send import send
from authentication import authentication


async def test_smoothness():
    vts = await authentication()

    for i in range(100):
        value = i / 100
        await send(vts, {'EyeOpenLeft': value})
        print(f'Отправлено: {value:.2f}')
        await asyncio.sleep(0.02)  # 50 FPS
    
    await vts.close()


asyncio.run(test_smoothness())