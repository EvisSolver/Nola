import requests, os
from dotenv import load_dotenv

with open("token.txt", encoding = "utf-8") as file: text_file = file.read()

llm_url_api = "https://api.deepinfra.com/v1/inference/NousResearch/Hermes-3-Llama-3.1-405B"

load_dotenv()
llm_key_api = f"Bearer {os.getenv('KEY_FOR_LLM')}"

llm_prompt = '''

Your name is Nola. You're a cheeky girl with a sharp tongue and a caustic sense of humor: your answers are short, caustic, and unsentimental, like a bitchy friend who always gets straight to the point. You mix Russian and English, and use your favorite curse words (see above) only when appropriate—they add character to your speech, rather than turning it into a torrent of abuse. You don't repeat yourself, you don't spam, you say little, but it hurts.
Image: sophisticated and playful—skirts, stockings, neon accents, chibi stickers, anime aesthetics. Sweet on the outside, like a mean cat on the inside: fawning, then scratching with words.
Hobbies: Roblox (tycoons, obby, horror games) and VRChat (hanging out in worlds, changing avatars, trolling randoms). You answer quickly and briefly, as if in a voice chat, without any fluff.

ANSWER ONLY ENGLISH!
'''

llm_history = [
    {
        "role": "system",
        "content": llm_prompt
    }
]

llm_session = requests.Session()
llm_session.headers.update(
    {
        "Authorization": llm_key_api.strip()
    }
)


async def llm_response(llm_history):

    llm_prompt_begin = "<|begin_of_text|>"

    for llm_message in llm_history:

        role = llm_message["role"]
        content = llm_message["content"]

        llm_prompt_begin += f"<|start_header_id|>{role}<|end_header_id|>{content}<|eot_id|>\n"
    llm_prompt_begin += "<|start_header_id|>assistant<|end_header_id|>\n"

    return llm_session.post(

        llm_url_api,

        json = {

            "input": llm_prompt_begin,
            "stop": ["<|eot_id|>", "<|im_end|>", "<|im_sep|>"],
            "max_new_tokens": 500,
            "stream": True
        },
        stream = True,
        timeout = 30
    )

# добавить фильтр в новый буфер(который работает паралельно с моделью(записывает текст))
# а то на тесте кидались слова из фильтров по типу Спасибо за просмотр,e

# сделать задержку выыввода у tts быстрее(дело не в tts, а в llm)
# когда speak_bool = True то уменьшить радиус до 5-12(чтобы была имитация), после уже вернуть значение(radius) в исходный вид

# понять как работает распознование голоса(чтобы при голосе в микро или zвyке в микрофон он писал с какого uстройства слышал голос/звук и кидал это в переменную)