import sqlite3
import streamlit as st
import pandas as pd

DB_PATH = "mboxdb.sqlite"

st.title("EMAIL - Stock")

search = st.text_input("Search for Email ex:text@ht.com")

conn = sqlite3.connect(DB_PATH)
if search:
    df = pd.read_sql("""
        SELECT varmb as email, countmb as tot
        FROM mbcount
        WHERE CAST(varmb AS TEXT) LIKE ? OR CAST(countmb AS TEXT) LIKE ?
    """, conn, params=(f"%{search}%", f"%{search}%"))
else:
    df = pd.read_sql("""
        SELECT varmb as email, countmb as tot
        FROM mbcount 
    """, conn)
conn.close()

st.dataframe(df, use_container_width=True)
st.caption(f"Showing {len(df)} rows")