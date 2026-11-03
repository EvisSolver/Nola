from pystyle import Colors, Write

from main_config import t_queue

from . import tts_response


def tts_logic(clean_text):

    response = tts_response.response(clean_text)

    if response.status_code != 200:
        Write.Print(f"tts_logic_py_log:L13: AT_TTS: Server Error: {response.status_code}\n", Colors.red_to_black, interval = 0)
        return None

    data = response.json()

    if "output_file_url" not in data:
        Write.Print(f"tts_logic_py_log:L19: AT_TTS: no audio on audio_server_response\n", Colors.red_to_black, interval = 0)
        return None
    
    return data["output_file_url"]


def tts_logic_text(text):

    if text is None:
        print("tts_test_py_log:L28: TTS gets NONE\n", flush = True)
        return None
    
    clean_text = text.replace("*", "").replace("_", "")

    if clean_text.strip() == "":
        print("tts_test_py_log:L28: text is empty: ''\n", flush = True)
        return None
    
    return clean_text