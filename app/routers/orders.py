from fastapi import APIRouter
from pydantic import BaseModel

class CustomerOrderIn(BaseModel):
    customer_id: int
    lines: list[dict] = []

router = APIRouter()

@router.post("/customer")
def create_customer_order(order: CustomerOrderIn):
    """Placeholder; students must persist and create outbound movements on confirm."""
    return {"status": "created", "order": order.model_dump()}
