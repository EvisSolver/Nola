PLUGIN_INFO = {
    'plugin_name': 'move',
    'developer': 'Evis',
    'requests_token': True,
    'authentication_token_path': './token.txt'
}

VTS_API_INFO = {
    'host': 'localhost',
    'port': 8001,
    'version': '1.0',
    'name': 'VTubeStudioPublicAPI'
}

async def request_parameters_api():

    return (
        PLUGIN_INFO,
        VTS_API_INFO
    )