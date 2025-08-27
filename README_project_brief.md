# Warehouse Database & Minimal App — Student Project Brief

## Context
You are a 4-person team hired by an agricultural company to design a **warehouse database** and a **minimal local app** (API + simple UI) to operate it. The owner (your teacher in role-play) is not a technical expert; requirements must be **elicited** and documented by the team.

## Goals (MVP)
- **DB (SQLite)**: robust ER design (constraints, indexes, views) + **data dictionary**.
- **API (FastAPI)**: endpoints for supplier→warehouse inbound, internal stock movements (in/out/transfer), customer orders.
- **UI (Streamlit)**: read-only tables for stock, orders, suppliers, customers; minimal forms to trigger core flows.
- **Docs (English)**: setup, usage, API contract, data dictionary, GDPR notes, RACI, retrospective.
- **GDPR**: identify personal data; **Google Form link** lives in the shared Drive. No real personal data in the repo.

## Tech & Environment
- Python 3.11.x
- Libraries: fastapi, uvicorn, sqlalchemy (2.x), pydantic (v2), streamlit, pytest, httpx, faker, requests
- DB: SQLite (default, file-based via SQLAlchemy). *(Optional advanced: MySQL via SQLAlchemy driver)*
- Editor: VS Code (extensions: Python, Pylance, REST Client, SQLite Viewer, Draw.io, GitHub PRs & Issues, Markdown All in One)

## Git Workflow & Branches
- Branches: **main**, **dev** (development), **test** (system testing), **prod** (release)
- Work on short-lived `feature/<scope>` branches → merge to `dev`. Promote `dev`→`test` via PR; if accepted, merge to `prod`. Final tag on `main`.

## Deliverables & Submission
- Upload a **ZIP of this repo** to the **shared Google Drive** in your group’s folder.
- Include: code, docs, ER diagram, tests, seed, slides, and a **link to your GitHub repo**. Include a text/markdown file with the **Google Form link** (privacy consent) stored in Drive.
- Naming: `ITS-GroupNN_WarehouseDB_v1.0_YYYYMMDD.zip`

## Definition of Done (high-level)
- DB: keys, FKs, uniqueness, indexes; **stock view** correct; **data dictionary** complete.
- API: endpoints documented (OpenAPI), validations + 4xx errors; orders confirm → outbound movements.
- UI: Streamlit shows stock, orders, suppliers, customers; minimal forms for inbound/outbound/transfer & order creation.
- Tests: stock math + key endpoints; seed deterministic.
- Docs & GDPR: setup/usage/API contract present; GDPR notes + Google Form link (in Drive).
- Process: RACI in repo; git flow followed (`dev`→`test`→`prod`, feature branches, PRs).
