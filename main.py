import asyncio, threading, warnings

from pystyle import Colors, Write

from main_config import t_queue

from llm import llm_answer, llm_config
from tts import tts_test

from whisper_stt import shared, transcribition, if_start_logic

from vts_model.vts_main import vts_main
from vts_model.mouth_smiling_for_tts import config_mouth
from vts_model.authentication import authentication


async def vts_model_main():
    vts = await authentication()
    await vts_main(vts)

def vts_run():
    asyncio.run(vts_model_main())


async def llm_worker():

    while True:
        user_input = await shared.llm_queue.get()

        shared.ai_is_talking = True
        llm_config.llm_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        Write.Print("main_py_log:L36: LLM thinking..\n", Colors.green, interval = 0)
        full_response = ""
        shared.ai_is_talking = True
        
        async for sentence in llm_answer.stream_sentences(llm_config.llm_history):
            full_response += sentence + " "
            t_queue.put(sentence)

        llm_config.llm_history.append(
            {
                "role": "assistant",
                "content": full_response.strip()
            }
        )

        config_mouth.mouth_start_bool = True
        await asyncio.to_thread(t_queue.join)
        await asyncio.to_thread(tts_test.audio_queue.join)
        config_mouth.mouth_close_bool = True
        Write.Print("main_py_log:L54: TTS sounded\n", Colors.green_to_blue, interval = 0)

        shared.ai_is_talking = False
        shared.llm_queue.task_done()


async def main():

    tts_thread = threading.Thread(target = tts_test.tts_worker)
    tts_thread.start()
    Write.Print("main_py_log:L63: TTS is started\n", Colors.green, interval = 0)

    await if_start_logic.if_start_logic()

    await asyncio.gather(
        transcribition.transcribe(),
        llm_worker()
    )

async def global_main():
    warnings.filterwarnings("ignore")

    vts_thread = threading.Thread(target = vts_run, daemon = True)
    vts_thread.start()

    await main()

asyncio.run(global_main())