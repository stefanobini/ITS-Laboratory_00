from fastapi import APIRouter
from pydantic import BaseModel, Field

class MovementIn(BaseModel):
    type: str = Field(..., description="IN | OUT | TRANSFER")
    product_id: int
    qty: float
    from_location_id: int | None = None
    to_location_id: int | None = None

router = APIRouter()

@router.post("")
def register_movement(mov: MovementIn):
    """Placeholder; students must implement stock consistency and validations."""
    return {"status": "accepted", "payload": mov.model_dump()}
