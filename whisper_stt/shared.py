import asyncio

llm_queue = asyncio.Queue()
tts_queue = asyncio.Queue()

stt_boolean = True
llm_boolean = None
tts_boolean = None

ai_is_talking = False