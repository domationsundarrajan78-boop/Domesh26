import streamlit as st
import sys
import os

# Fix import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Import your modules
from pipeline.generator import generate_log
from pipeline.parser import parse_log
from pipeline.processor import process_log

# Title
st.set_page_config(page_title="Log Monitoring", layout="wide")
st.title("🔍 Log Monitoring Dashboard")

# Generate logs
logs = []

num_logs = st.slider("Select number of logs", 10, 500, 50)

for i in range(num_logs):
    raw = generate_log()
    parsed = parse_log(raw)
    processed = process_log(parsed)

    if processed:
        logs.append(processed)

# 🔥 Convert to table
import pandas as pd
df = pd.DataFrame(logs)

# 📊 Metrics
col1, col2 = st.columns(2)

error_count = df[df["level"].isin(["ERROR", "CRITICAL"])].shape[0]
total_logs = len(df)

col1.metric("📄 Total Logs", total_logs)
col2.metric("🚨 Error Logs", error_count)

# 📄 Show logs table
st.subheader("📄 Logs Table")

# Highlight errors
def highlight_errors(row):
    if row["level"] in ["ERROR", "CRITICAL"]:
        return ["background-color: red"] * len(row)
    return [""] * len(row)

st.dataframe(df.style.apply(highlight_errors, axis=1))

# 📊 Chart
st.subheader("📊 Log Level Distribution")

chart_data = df["level"].value_counts()
st.bar_chart(chart_data)

# 🔁 Auto refresh button
if st.button("🔄 Refresh Logs"):
    st.rerun()
    