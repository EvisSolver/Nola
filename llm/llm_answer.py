import json
from pystyle import Colors, Write
from . import llm_config


async def stream_sentences(llm_history):

    llm_response = await llm_config.llm_response(llm_history)  # объект стрим-ответа
    buffer = ""  # накапливает токены

    for llm_line in llm_response.iter_lines():  # читаем построчно

        if not llm_line.startswith(b"data: "):
            continue

        data = json.loads(llm_line[6:])  # парсим JSON
        token = data.get("token", {}).get("text", "")

        if not token:
            continue

        buffer += token

        # проверяем есть ли . ! или ? в буфере
        while True:
            dot_idx = -1
            for punct in ".!?":
                pos = buffer.find(punct)
                # пропускаем если это .. или !! или ??
                while pos != -1 and pos+1 < len(buffer) and buffer[pos+1] == punct:
                    pos = buffer.find(punct, pos+1)
                if pos != -1 and (dot_idx == -1 or pos < dot_idx):
                    dot_idx = pos

            if dot_idx == -1:  # знаков нет - ждём дальше
                break

            sentence = buffer[:dot_idx + 1].strip()  # вырезаем до знака
            buffer = buffer[dot_idx + 1:].lstrip()   # остаток

            if sentence:
                Write.Print(f"Sentence: {sentence}\n\n", Colors.yellow, interval=0)
                yield sentence

    if buffer.strip():  # остаток без знака
        yield buffer.strip()