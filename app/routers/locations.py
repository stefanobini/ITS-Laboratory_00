from fastapi import APIRouter
router = APIRouter()

@router.get("")
def list_locations():
    """Placeholder endpoint — returns an empty list until implemented."""
    return []
