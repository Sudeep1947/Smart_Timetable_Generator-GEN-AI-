
from fastapi import APIRouter
from backend.core.scheduler import detect_conflict

router = APIRouter()

@router.post("/check-conflict")
def check_conflict(event: dict):
    conflict = detect_conflict(event)
    return {"conflict": conflict}
