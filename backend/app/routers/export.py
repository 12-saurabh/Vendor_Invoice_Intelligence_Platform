from fastapi import APIRouter

router = APIRouter(
    prefix="/export",
    tags=["Export"]
)

@router.get("/")
def export_home():
    return {"message": "Export module is working"}