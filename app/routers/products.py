from fastapi import APIRouter
router = APIRouter()

@router.get("")
def list_products():
    """Placeholder endpoint — returns an empty list until implemented."""
    return []
