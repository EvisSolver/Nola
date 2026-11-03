import asyncio, queue

import numpy as np

from pystyle import Colors, Write

from . import whisper_config, vad_model, whisper_model, if_filter
from . import shared


async def transcribe():

    whisper_config.audio_queue = queue.Queue()

    while True:

        raw = await asyncio.to_thread(whisper_config.audio_queue.get)

        if shared.stt_boolean == False:

            whisper_config.full_text = ''
            whisper_config.has_speech_boolean = False
            whisper_config.when_silence_sec = 0

            continue


        audio_data = raw.flatten().astype(np.float32)


        if not await vad_model.vad_has_speech(audio_data):
            whisper_config.when_silence_sec += whisper_config.chunk_duration

            if whisper_config.when_silence_sec >= 2:
                if whisper_config.has_speech_boolean == True:

                    text = whisper_config.full_text.strip()
                    print(text)

                    if shared.ai_is_talking == True:
                        whisper_config.ai_talking_text += (' ' + text)

                    elif shared.ai_is_talking == False:

                        final_request = (f"|КОММЕНТАРИЙ| {whisper_config.ai_talking_text} |КОММЕНТАРИЙ| {text}").strip()
                        
                        Write.Print(f"main_py_log:L42: final_request: {final_request}\n", Colors.purple, interval = 0)
                        await shared.llm_queue.put(final_request)
                        whisper_config.ai_talking_text = ''


                    whisper_config.full_text = ''

                    whisper_config.has_speech_boolean = False
                    whisper_config.when_silence_sec = 0
                    whisper_config.filter_boolean = False
                #     if shared.stt_boolean == False:
                #         print('stt skipped:')
                #         whisper_config.full_text = ''
                #         whisper_config.has_speech_boolean = False
                #         continue
                #     await shared.llm_queue.put(text)
                #     shared.stt_boolean = False
                #     shared.llm_boolean = True
                    whisper_config.full_text = ''
                    whisper_config.has_speech_boolean = False

            else:
                print("didn't recognize")
                whisper_config.when_silence_sec = 0
            continue

        else:
            print('recognize')

            whisper_config.when_silence_sec = 0
            whisper_config.has_speech_boolean = True

            segments, _ = whisper_model.model.transcribe(

                audio_data,
                language = whisper_config.whisper_language,
                beam_size = 1
            )

            for i in segments:

                filtered_text = if_filter.filter_torchok(i.text)

                if whisper_config.filter_boolean == True:
                    whisper_config.full_text += (' ' + filtered_text.strip())
