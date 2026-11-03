from . import tts_test


async def tts_main():

    while True:
        
        text = str(input())
        
        await tts_test.speak(text)