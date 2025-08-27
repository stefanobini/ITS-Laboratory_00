# Usage

## Common flows
- View **stock**: open Streamlit and click "Load stock KPI".
- Post an **inbound** movement: use the form in Streamlit; the API receives `POST /movements` with type=IN.
- Create a **customer order**: to be implemented by the team (`POST /orders/customer` + lines + confirm).

## API docs
When the API is running, visit `/docs` (Swagger UI) or `/redoc` for OpenAPI.

## Notes
- The current endpoints are placeholders; the team must implement persistence and validations.
- The **stock view** should reflect IN/OUT/TRANSFER logic and be exposed under `/kpi/stock`.
