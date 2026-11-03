import requests, io, queue, threading

import sounddevice as sd
import soundfile as sf

from pystyle import Colors, Write

from . import config_tts
from . import tts_logic

from vts_model.mouth_smiling_for_tts import config_mouth

from main_config import t_queue


audio_queue = queue.Queue()

def tts_generate_worker():
    print("tts_test_py_log:L19: TTS gen is started\n", flush = True)

    session = requests.Session()

    while True:
        text = t_queue.get()
        if text is None:
            audio_queue.put(None)
            t_queue.task_done()
            break

        clean_text = tts_logic.tts_logic_text(text)

        if clean_text is None:
            t_queue.task_done()
            continue
        
        print(f"tts_test_py_log:L36: LLM generate: {clean_text}\n", flush = True)
        audio_url_data = tts_logic.tts_logic(clean_text)
        wav_bytes = session.get(audio_url_data)

        if audio_url_data is None:
            t_queue.task_done()
            continue

        wav_bytes = session.get(audio_url_data, timeout = 60).content
        audio, samplerate = sf.read(io.BytesIO(wav_bytes))

        audio_queue.put(
            (
                audio, samplerate
            )
        )

        t_queue.task_done()

def tts_play_worker():
    print("tts_test_py_log:L56: TTS play'er is started\n", flush = True)

    while True:
        item = audio_queue.get()

        if item is None:
            audio_queue.task_done()
            break

        audio, samplerate = item

        print(f"tts_speak: {config_mouth.mouth_start_bool}")

        sd.play(
            audio,
            samplerate = samplerate,
            device = config_tts.cable_name
        )
        sd.wait()
        audio_queue.task_done()


def tts_worker():
    gen = threading.Thread(target = tts_generate_worker, daemon = True)
    play = threading.Thread(target = tts_play_worker, daemon = True)

    gen.start()
    play.start()

    gen.join()
    play.join()