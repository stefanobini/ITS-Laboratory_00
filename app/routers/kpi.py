from fastapi import APIRouter
router = APIRouter()

@router.get("/stock")
def stock_kpi():
    """Placeholder KPI endpoint — students will compute live/aggregated stock."""
    return {"items": []}
