from . import whisper_config


async def clear_whisper():

    whisper_config.has_speech_boolean = False
    whisper_config.full_text = ''
    whisper_config.when_silence_sec = 0