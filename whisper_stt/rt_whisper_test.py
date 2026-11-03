import numpy as np, soundcard as sc, queue, threading, torch

from faster_whisper import WhisperModel


samplerate = 16000
chunc_sec = 3
frames_per_chunk = int(samplerate * chunc_sec)

audio_queue = queue.Queue()

model = WhisperModel(

    'large-v3',
    device = 'cuda',
    compute_type = 'int8'
)

vad_model, utils = torch.hub.load(

    repo_or_dir = 'snakers4/silero-vad',
    model = 'silero_vad'
)


get_speech_timestamps = utils[0]


def has_speech(audio):

    audio_tensor = torch.from_numpy(audio).float()

    timestamps = get_speech_timestamps(

        audio_tensor,
        vad_model,
        sampling_rate = samplerate
    )

    return len(timestamps) > 0


def capture_system_audio():

    speaker = sc.default_speaker()

    print(f'Capturing audio from: {speaker}')

    with sc.get_microphone(

        id = str(speaker.id),
        include_loopback = True
    ).recorder(

        samplerate = samplerate,
        channels = 1
    ) as mic:
        
        while True:

            data = mic.record(numframes = frames_per_chunk)
            audio_queue.put(data)


def start_transcribition():

    while True:

        audio_data = audio_queue.get().flatten().astype(np.float32)

        if not has_speech(audio_data):
            continue

        segments, _ = model.transcribe(

            audio_data,
            language = 'ru',
            beam_size = 1
        )

        for segment in segments:

            text = segment.text

            print(text)


threading.Thread(

    target = capture_system_audio, 
    daemon = True
    ).start()


start_transcribition()