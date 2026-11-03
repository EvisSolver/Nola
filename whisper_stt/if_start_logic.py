import threading

import soundcard as sc

from . import speakers_detector, microphone_detector
from . import clear_whisper


async def if_start_logic():

    await clear_whisper.clear_whisper()

    while True:

        raw = input('1 - microphone\n2 - speakers\n')

        if raw not in ('1', '2'):

            print('only 1 or 2 possible rn')
            continue

        pick = int(raw)

        if pick == 1:
            
            device = sc.default_microphone()
            threading.Thread(

                target = microphone_detector.microphone_detector,
                args = (device,),

                daemon = True
                
            ).start()
            break

        elif pick == 2:

            device = sc.default_speaker()
            threading.Thread(

                target = speakers_detector.speakers_detector,
                args = (device,),

                daemon = True

            ).start()
            break

        else:
            print('only 1 or 2 is possible rn')

            # сделать чтобы после выбора постоянно стоял либо микро(1) либо спикер(2)
            # посмотреть как будет, и если что добавить очередь:
            # пока говорит tts - виспер ничего не записывает(либо обнуляет после озвучки)
            # дальше сам догадаешься