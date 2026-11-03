from faster_whisper import WhisperModel

model_size = 'small'

model = WhisperModel(model_size, device = 'cuda', compute_type = 'float16')

segments, info = model.transcribe('audio.mp3',
                                  language = 'ru',
                                  beam_size = 5)

for segment in segments:
    print(segment.text)