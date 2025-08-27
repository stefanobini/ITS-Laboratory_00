# Setup

## Prerequisites
- Python 3.11.x
- VS Code (recommended extensions: Python, Pylance, REST Client, SQLite Viewer, Draw.io Integration, GitHub PRs & Issues, Markdown All in One)

## 1) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

## 2) Install dependencies
```bash
pip install -r requirements.txt
```

## 3) Configure environment
Copy `.env.example` to `.env` and adjust if needed. Default DB is local SQLite (`magazzino.db`).

## 4) Run the API
```bash
uvicorn app.main:app --reload
```

## 5) Run the Streamlit UI (new terminal)
```bash
streamlit run ui/app.py
```

## Optional: switch to MySQL
- Install a MySQL server locally and the driver (`pip install pymysql`)
- Set `DATABASE_URL=mysql+pymysql://user:pass@localhost/dbname` in `.env`
- Update models & engine accordingly
