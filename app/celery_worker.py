from celery import Celery

# Celery application
celery_app = Celery(
    "vendor_invoice_platform",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Automatically discover tasks
celery_app.autodiscover_tasks(["app"])