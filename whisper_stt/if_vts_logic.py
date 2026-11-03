import asyncio

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import vts_model.mouth_smile_logic.main_mouth_smile
import vts_model.mouth_sadding_logic.main_mouth_sad
import vts_model.authentication

happy = {

    'улыбнись',
    'радость',
    'можешь улыбнуться'
}

sad = {

    'загрусти',
    'грусти',
    'грусть',
    'грустно'
}

async def vts_logic(full_text):

    vts = await vts_model.authentication.authentication()

    clean_vts_message = full_text.strip().lower().rstrip('.,!?')

    if clean_vts_message in happy:

        await vts_model.mouth_smile_logic.main_mouth_smile.main_mouth_smilling(vts)

        print('smiling..')


    elif clean_vts_message in sad:

        await vts_model.mouth_sadding_logic.main_mouth_sad.main_mouth_sadding(vts)
            
        print('sadding..((')