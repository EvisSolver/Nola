from silero_vad import load_silero_vad, get_speech_timestamps
from . import whisper_config
import torch

vad_model = load_silero_vad()  # модель уже внутри пакета, сеть не нужна

async def vad_has_speech(audio):
    audio_tensor = torch.from_numpy(audio).float()
    timestamps = get_speech_timestamps(
        audio_tensor, vad_model, sampling_rate=whisper_config.samplerate
    )
    return len(timestamps) > 0