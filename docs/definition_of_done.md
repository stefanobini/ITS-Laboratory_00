# Definition of Done

## DB
- Keys, FKs, uniqueness in place; **no orphan records**.
- Indexes on frequent queries; **stock view** is correct.
- Data dictionary complete and consistent with schema.

## API
- Endpoints implemented and documented (OpenAPI).
- Validations + meaningful error codes (4xx).
- Confirming a customer order generates outbound movements.

## UI
- Streamlit: stock, orders, suppliers, customers tables visible.
- Minimal forms for inbound/outbound/transfer and order creation.

## Tests & Seed
- Unit & API tests for core logic pass.
- Seed deterministic (fixed random seed).

## Docs & GDPR
- Setup/usage/API contract present and accurate.
- GDPR notes included; Google Form link referenced.

## Process
- RACI present; git workflow respected (`main/dev/test/prod`, PRs).
