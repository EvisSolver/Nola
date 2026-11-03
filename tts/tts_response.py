import requests

from . import config_tts


def response(clean_text):

    response = config_tts.session.post(

        f"{config_tts.alltalktts_url}/api/tts-generate",

        data = {

            "text_input": clean_text,
            "text_filtering": "standard",
            "text_not_inside": "character",

            "character_voice_gen": config_tts.tts_character_voice,
            
            "language": config_tts.tts_language,

            "narrator_enabled": "false",
            "narrator_voice_gen": "male_01.wav",

            "output_file_name": "output",
            "output_file_timestamp": "true",
            
            "autoplay": "false",
            "autoplay_volume": "0.8",
        },
        timeout = 90
    )

    return response