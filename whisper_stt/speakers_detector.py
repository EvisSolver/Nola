import soundcard as sc
from . import whisper_config

def speakers_detector(speaker):
    # Напрямую подключаемся к loopback-каналу наушников G733 по его уникальному ID
    speaker = sc.get_microphone(

        id = whisper_config.get_microphone_id, 
        include_loopback=True
    )

    print(f'speakers picks on: {speaker.name}')

    with speaker.recorder(

        samplerate=whisper_config.samplerate, 
        channels=1
    ) as speakers:
        while True:

            data = speakers.record(

                numframes=whisper_config.frames_per_chunk
            )
            whisper_config.audio_queue.put(data)
