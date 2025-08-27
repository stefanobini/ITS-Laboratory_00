# REPO GUIDE — Warehouse DB & Minimal App

This guide explains **where things live** in the repository and **where to add your work**. Keep it simple, keep it consistent.

---

## 1) Repository Map — “Where to find / put things”

```
.
├─ app/                  # FastAPI (backend)
│  ├─ main.py            # App entrypoint (mounts routers, /health)
│  ├─ database.py        # SQLAlchemy engine (SQLite by default), Session
│  ├─ models.py          # ORM models (tables, FKs, indexes)  ← DB SCHEMA HERE
│  ├─ schemas.py         # Pydantic models for requests/responses
│  └─ routers/           # One router per domain (implement endpoints here)
│     ├─ products.py
│     ├─ partners.py
│     ├─ locations.py
│     ├─ movements.py
│     ├─ orders.py
│     └─ kpi.py
│  └─ tests/             # pytest tests (unit + API)
│     └─ test_*.py
├─ ui/
│  └─ app.py             # Streamlit minimal UI (tables + simple forms)
├─ seed/
│  └─ seed.py            # Deterministic synthetic data (Faker)
├─ docs/                 # Documentation (EN)  ← KEEP THESE UPDATED
│  ├─ README_setup.md    # How to install & run (API, UI)
│  ├─ README_usage.md    # Typical flows + API docs link
│  ├─ api_contract.md    # Endpoints, payloads, errors
│  ├─ data_dictionary.md # Tables, columns, constraints, views
│  ├─ gdpr_notes.md      # Personal data, minimization, Form link reference
│  ├─ raci.md            # Roles & responsibilities
│  └─ definition_of_done.md
├─ diagram.drawio        # Team ER diagram
├─ requirements.txt      # Python deps
├─ .env.example          # Example env (copy to .env)
└─ START_HERE.md / REPO_GUIDE.md (this file)
```

**Golden rule:**  
When you change something in `app/models.py` (schema), you also update:
- `docs/data_dictionary.md` (columns, FKs, indexes, views)  
- `diagram.drawio` (ER)  
- any affected routers/schemas/tests

---

## 2) Quick Start — “How to run it locally”

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env

# Terminal A — API
uvicorn app.main:app --reload

# Terminal B — UI
streamlit run ui/app.py
```

- API docs: open `http://127.0.0.1:8000/docs` (Swagger).
- Health check: `GET /health`.

---

## 3) What goes where (by task)

### A) Add / modify a TABLE
1. Define in `app/models.py` (PK, FKs, unique, indexes, nullability).
2. Update `docs/data_dictionary.md` and `diagram.drawio`.
3. If needed, expose read/write endpoints in a router (see B).
4. Extend seed in `seed/seed.py` and tests in `app/tests/`.

### B) Add an ENDPOINT
1. Define request/response in `app/schemas.py`.
2. Implement logic in the correct `app/routers/*.py`.
3. Add tests in `app/tests/` (unit and/or TestClient).
4. Document in `docs/api_contract.md`.

### C) Update STOCK / KPI
- Compute stock from movements (IN/OUT/TRANSFER).
- Expose it at `GET /kpi/stock`.
- Show it in Streamlit tables (`ui/app.py`).

### D) Seed data
- Implement deterministic seed in `seed/seed.py` (use Faker + fixed random seed).
- **No real personal data** in the repo.

---

## 4) Branches — simple manual usage (no strict rules)

- **main**: canonical end-of-course state (final tag).
- **dev**: daily development (most changes land here).
- **test**: team testing / internal stabilization.
- **prod**: your “release” branch before delivery.

**Suggested (manual) flow**:
- Work on a small **feature branch** (`feature/short-name`), then merge into **`dev`**.
- When `dev` is stable, merge into **`test`** for group testing.
- When tests & demo are OK, merge `test` → **`prod`**.
- At the end, create the final tag and align **`main`**.

Examples:
```bash
git checkout -b feature/movements
# ... commit work ...
git checkout dev
git merge feature/movements
git push origin dev

# later
git checkout test
git merge dev
git push origin test

# release
git checkout prod
git merge test
git push origin prod

# final tag on main (end of course)
git checkout main
git merge prod
git tag -a v1.0.0 -m "Final delivery"
git push origin main --tags
```

> Keep it **manual and simple**: talk to your teammates before merging between branches.

---

## 5) Docs & GDPR — keep in sync
- Every feature that touches schema or API must update:
  - `docs/data_dictionary.md`  
  - `docs/api_contract.md`  
  - `docs/README_usage.md` (if flow changes)
- **GDPR**: keep `docs/gdpr_notes.md` updated and **store the Google Form in Drive**.  
  In the final ZIP, add a small text/markdown file that contains the **link** to the Form in Drive.

---

## 6) Tests — minimum expectation
- **Unit**: stock math (IN/OUT/TRANSFER), non-negative stock, basic rules.
- **API**: create/list entities; inbound updates stock; order confirm ⇒ outbound; invalid ops ⇒ `4xx`.
- Run with:
```bash
pytest -q
```

---

## 7) Submission — what & where
- Create a ZIP of the repo:  
  `ITS-GroupNN_WarehouseDB_v1.0_YYYYMMDD.zip`
- Upload to your group’s folder in **Drive** under `group_deliveries/Group-XX/`.
- Include:
  - code, docs, ER, tests, seed  
  - slides (PDF) for the demo  
  - a text/markdown file with the **Google Form link** (privacy consent)  
  - a link to your **remote GitHub repo**

---

## 8) Troubleshooting (quick)
- **API not reachable?** Check `uvicorn` terminal and `.env` (`API_HOST`, `API_PORT`).
- **SQLite locked?** Stop the API/UI, close DB viewers, re-run.
- **Streamlit cannot load KPI?** Implement `/kpi/stock` and verify with REST Client or Swagger.
- **Import errors?** Activate the venv and reinstall `requirements.txt`.

Happy building!
