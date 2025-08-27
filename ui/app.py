"""Minimal Streamlit UI: calls FastAPI /health and shows placeholders.

Run:
    streamlit run ui/app.py
"""
import os
import requests
import streamlit as st

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", "8000")
API_URL = f"http://{API_HOST}:{API_PORT}"

st.set_page_config(page_title="Warehouse UI", layout="wide")
st.title("Warehouse — Minimal UI")

# Health
try:
    health = requests.get(f"{API_URL}/health", timeout=2).json()
    st.success(f"API health: {health}")
except Exception as e:
    st.error(f"Cannot reach API at {API_URL} — start it with: uvicorn app.main:app --reload")

st.header("Stock (placeholder)")
if st.button("Load stock KPI"):
    try:
        data = requests.get(f"{API_URL}/kpi/stock", timeout=5).json()
        st.write(data)
    except Exception as e:
        st.error(str(e))

st.header("Quick Operations (placeholders)")
with st.form("inbound_form"):
    st.subheader("Inbound (from supplier)")
    product_id = st.number_input("Product ID", min_value=1, step=1)
    qty = st.number_input("Quantity", min_value=0.0, step=1.0)
    to_loc = st.number_input("To location ID", min_value=1, step=1)
    submitted = st.form_submit_button("Post IN movement")
    if submitted:
        payload = {"type": "IN", "product_id": int(product_id), "qty": float(qty), "to_location_id": int(to_loc)}
        r = requests.post(f"{API_URL}/movements", json=payload)
        st.write(r.status_code, r.json())
