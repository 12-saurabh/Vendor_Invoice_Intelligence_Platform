
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


# Database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Vendor Invoice Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Vendor Invoice Intelligence Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)




# ==============================
# ROUTERS
# ==============================


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



# ==============================
# PROMETHEUS
# ==============================


Instrumentator().instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False
)