import asyncio

# глобальная блокировка для WebSocket
websocket_lock = asyncio.Lock()