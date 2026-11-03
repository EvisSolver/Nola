import requests


session = requests.Session()
alltalktts_url = 'http://127.0.0.1:7851'
cable_name = "pulse"

tts_speak = False

tts_language = 'en'
tts_character_voice = "VO_Ganyu_About_the_Vision.wav"