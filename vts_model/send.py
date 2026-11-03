from .shared import websocket_lock

async def send(vts, params: dict = {}):
    async with websocket_lock:
        await vts.request(
            {
                'apiName': 'VTubeStudioPublicAPI',
                'apiVersion': '1.0',
                'requestID': 'move',
                'messageType': 'InjectParameterDataRequest',
                'data':
                {
                    'faceFound': True,
                    'mode': 'set',
                    'parameterValues': [
                        {
                            'id': k,
                            'value': v
                        }
                        for k, v in params.items()
                    ]
                }
            }
        )