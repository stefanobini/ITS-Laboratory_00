"""FastAPI application entrypoint.

Run in dev:
    uvicorn app.main:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import products, partners, locations, movements, orders, kpi

app = FastAPI(title="Warehouse API", version="0.1.0")

# CORS (local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "warehouse-api"}

# Routers (placeholders; students will implement the logic)
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(partners.router, prefix="/partners", tags=["partners"])
app.include_router(locations.router, prefix="/locations", tags=["locations"])
app.include_router(movements.router, prefix="/movements", tags=["movements"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(kpi.router, prefix="/kpi", tags=["kpi"])
