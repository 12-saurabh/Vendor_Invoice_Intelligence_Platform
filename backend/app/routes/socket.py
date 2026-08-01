from fastapi import APIRouter,WebSocket

from app.websocket.manager import manager


router=APIRouter()



@router.websocket("/notifications")
async def websocket_endpoint(
    websocket:WebSocket
):

    await manager.connect(websocket)


    while True:

        data=await websocket.receive_text()

        await manager.broadcast(data)