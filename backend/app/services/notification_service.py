
from app.websocket_manager import manager


async def notify_invoice_uploaded(
    invoice_id: int,
    invoice_number: str,
    file_name: str,
):
    await manager.broadcast(
        {
            "type": "INVOICE_UPLOADED",
            "message": "New invoice uploaded",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "file_name": file_name,
            "status": "Processing",
        }
    )


async def notify_invoice_approval_required(
    invoice_id: int,
    invoice_number: str,
):
    await manager.broadcast(
        {
            "type": "INVOICE_APPROVAL_REQUIRED",
            "message": "Invoice requires manual approval",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
        }
    )


async def notify_invoice_approved(
    invoice_id: int,
    invoice_number: str,
):
    await manager.broadcast(
        {
            "type": "INVOICE_APPROVED",
            "message": "Invoice approved",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
        }
    )


async def notify_invoice_rejected(
    invoice_id: int,
    invoice_number: str,
):
    await manager.broadcast(
        {
            "type": "INVOICE_REJECTED",
            "message": "Invoice rejected",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
        }
    )


async def notify_prediction_completed(
    invoice_id: int,
    invoice_number: str,
):
    await manager.broadcast(
        {
            "type": "PREDICTION_COMPLETED",
            "message": "Invoice prediction completed",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
        }
    )


async def notify_invoice_failed(
    invoice_id: int,
    invoice_number: str,
    error: str,
):
    await manager.broadcast(
        {
            "type": "INVOICE_PROCESSING_FAILED",
            "message": "Invoice processing failed",
            "invoice_id": invoice_id,
            "invoice_number": invoice_number,
            "error": error,
        }
    )

