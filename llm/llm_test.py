import requests, json, os
from dotenv import load_dotenv

load_dotenv()
url_key = 'https://api.deepinfra.com/v1/inference/NousResearch/Hermes-3-Llama-3.1-70B'
llm_key = os.getenv()

prompt = ''''''


while True:
    user_input = input("\nYou: ")

    if not user_input.strip(): #  Если пользователь нажал Enter ничего не введя - пропускаем итерацию, не отправляем пустой запрос.
        continue

    prompt = f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>тебя зовут Нола. Ты полезный ассистент. ты очень хорошо разбираешься в психологии и в юморе, иногда у тебя очень длинный язык.<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"

    llm_response = requests.post(

        'https://api.deepinfra.com/v1/inference/NousResearch/Hermes-3-Llama-3.1-70B',
        
        headers={"Authorization": f'Bearer {llm_key}'},
            json={"input": prompt, "stop": ["<|eot_id|>", "<|im_end|>", "<|im_sep|>"], "stream": True},
            stream=True, timeout=15
    )

    print("Assistant: ", end="", flush=True)

    for line in llm_response.iter_lines():
        
        if line.startswith(b'data'):

            token = json.loads(

            line[5:]
            )['token']['text']

            print(token, end = '', flush = True)