import soundcard as sc
from . import whisper_config

def microphone_detector(microphone):
    # На Linux pythoncom.CoInitialize() не требуется и удален
    microphone = sc.default_microphone()

    print(f'microphone picks on: {microphone.name}')

    with sc.get_microphone(
        id=microphone.id,
        include_loopback=True
    ).recorder(
        samplerate=whisper_config.samplerate,
        channels=1
    ) as m_recorder:  # Переименовано, чтобы избежать конфликта имен с аргументом
        
        while True:
            data = m_recorder.record(
                numframes=whisper_config.frames_per_chunk
            )
            whisper_config.audio_queue.put(data)