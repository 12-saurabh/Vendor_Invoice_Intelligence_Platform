from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.websocket_manager import manager


router = APIRouter(
    tags=["WebSocket"]
)


@router.websocket("/ws/dashboard")
async def websocket_dashboard(
    websocket: WebSocket,
):
    await manager.connect(websocket)

    try:
        while True:
            # Keep the connection alive and allow
            # the client to send messages.
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(websocket)

    except Exception:
        manager.disconnect(websocket)

@router.post("/ws/test")
async def test_websocket():
    await manager.broadcast(
        {
            "type": "TEST",
            "message": "WebSocket notification is working"
        }
    )

    return {
        "message": "Notification sent"
    }