import queue


samplerate = 16000

chunk_sec = 2
frames_per_chunk = int(samplerate * chunk_sec)

audio_queue = queue.Queue()


filter_boolean = True

whisper_language = 'en'

full_text = ''
whisper_text_for_llm_live = ''

ai_talking_text = ''


when_silence_sec_limit = 2
when_silence_sec = 0
chunk_duration = frames_per_chunk / samplerate
has_speech_boolean = None

get_microphone_id = 'alsa_output.usb-Logitech_G733_Gaming_Headset_0000000000000000-00.analog-stereo.monitor'