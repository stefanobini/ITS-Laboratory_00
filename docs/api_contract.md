# API Contract (to be completed by the team)

## Health
- `GET /health` → `{"status":"ok","service":"warehouse-api"}`

## Products
- `GET /products` → `[]` (placeholder, to be replaced with DB-backed data)
- `POST /products` → create product (schema TBD)

## Partners (suppliers/customers)
- `GET /partners` → `[]` (placeholder)

## Locations
- `GET /locations` → `[]` (placeholder)

## Movements
- `POST /movements` (type IN|OUT|TRANSFER, validations TBD)

## Orders
- `POST /orders/customer` (create)
- `POST /orders/customer/{id}/confirm` (generate OUT movements)

## KPI
- `GET /kpi/stock` → stock by product/location
