# tts_test.py
import io
import sounddevice as sd
import soundfile as sf

from . import config_tts


# создаёт объект-сессию, который держит одно TCP-соединение вместо того чтобы открывать/закрывать на каждый запрос
session = config_tts.session

async def speak(text, voice = 'фывanimewkakr.wav', language = 'ru'):

    response = session.post(
        
        f'{config_tts.alltalktts_url}/api/tts-generate',

        data = {

            'text_input': text,
            'text_filtering': 'standard',
            'character_voice_gen': voice,
            'narrator_enabled': 'false',
            'narrator_voice_gen': 'male_01.wav',
            'text_not_inside': 'character',
            'language': language,
            'output_file_name': 'output',
            'output_file_timestamp': 'true',
            'autoplay': 'false',
            'autoplay_volume': '0.8',
            'deepspeed_activate': 'true'
        },

        timeout = 10,
    )

 
    # проверка статуса сервера(локалки самой)
    response.raise_for_status()

    # вытаскивает ссылку на WAV из ответа сервера. response.json() парсит JSON, ['output_file_url'] берёт значение по ключу
    url = response.json()['output_file_url']

    # забираем готовый wav прямо в память (не сохраняем на диск)
    # GET-запрос по тому же TCP-соединению (не открывает новое). .content — сырые байты WAV-файла в памяти
    wav_bytes = session.get(url, timeout = 10).content


    audio, samplerate = sf.read(io.BytesIO(wav_bytes)) # декодирует байты в numpy-массив


    sd.play(audio, samplerate = samplerate, device = config_tts.cable_name)
    sd.wait()