import pyvts

from .api_parameters import PLUGIN_INFO, VTS_API_INFO
from pystyle import Colors, Write


async def authentication():

    vts = pyvts.vts(plugin_info = PLUGIN_INFO, vts_api_info = VTS_API_INFO)

    await vts.connect()
    await vts.request_authenticate_token()
    await vts.request_authenticate()
        
    Write.Print('Connected\n', Colors.green, interval = 0.02)

    return vts