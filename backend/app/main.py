from fastapi import FastAPI
from app.database import Base, engine
from prometheus_fastapi_instrumentator import Instrumentator
from app.routers import (
    vendor,
    invoice,
    auth,
    upload,
    approval,
    prediction,
    dashboard,
    audit,
    timeline,
    notification,
    analytics,
    search,
    websocket,
    report,
    admin,
    export
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vendor Invoice Intelligence Platform",
    description="""
## Production-ready Vendor Invoice Management System

### Features
- JWT Authentication
- Vendor Management
- Invoice OCR
- ML Predictions
- Approval Workflow
- Dashboard Analytics
- Reports
- CSV / Excel / PDF Export
- WebSocket Notifications
- Prometheus Metrics

""",
    version="1.0.0",
    contact={
        "name": "Saurabh Kumar",
        "email": "your_email@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

app.include_router(vendor.router)
app.include_router(invoice.router)
app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(approval.router)
app.include_router(prediction.router)
app.include_router(dashboard.router)
app.include_router(audit.router)
app.include_router(timeline.router)
app.include_router(notification.router)
app.include_router(analytics.router)
app.include_router(search.router)
app.include_router(websocket.router)
app.include_router(report.router)
app.include_router(admin.router)
app.include_router(export.router)

Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False
)