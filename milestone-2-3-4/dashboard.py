import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import sys
import os

# Fix import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))

# Import pipeline
from pipeline.generator import generate_log
from pipeline.parser import parse_log
from pipeline.processor import process_log

# Detection + Alert
from detection.anomaly import detect_anomaly
from detection.alert import send_alert


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Log Monitoring", layout="wide")
st.title("🔍 Log Monitoring Dashboard")


# =========================
# SIDEBAR
# =========================
st.sidebar.title("🔧 Filters")

services = ["auth", "payment", "db", "api"]
selected_services = st.sidebar.multiselect("Service", services)

levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
selected_levels = st.sidebar.multiselect("Level", levels)

show_only_anomalies = st.sidebar.checkbox("Show only anomalies")


# =========================
# FILTER FUNCTION
# =========================
def filter_logs(logs):
    filtered = []

    for log in logs:
        if selected_services and log["service"] not in selected_services:
            continue
        if selected_levels and log["level"] not in selected_levels:
            continue
        filtered.append(log)

    return filtered


# =========================
# LIVE LOG GENERATION
# =========================
if "logs" not in st.session_state:
    st.session_state.logs = []

raw = generate_log()
parsed = parse_log(raw)
processed = process_log(parsed)

if processed:
    st.session_state.logs.append(processed)

logs = st.session_state.logs[-200:]  # keep last 200


# =========================
# APPLY FILTER
# =========================
filtered_logs = filter_logs(logs)

if show_only_anomalies:
    filtered_logs = [log for log in filtered_logs if log["level"] in ["ERROR", "CRITICAL"]]

df = pd.DataFrame(filtered_logs)


# =========================
# ANOMALY DETECTION
# =========================
new_anomaly = []

if processed and processed["level"] in ["ERROR", "CRITICAL"]:
    new_anomaly.append(processed)
anomalies = detect_anomaly(logs)


# =========================
# EMAIL ALERT (COOLDOWN)
# =========================
if "last_alert_time" not in st.session_state:
    st.session_state.last_alert_time = 0

current_time = time.time()

if new_anomaly and current_time - st.session_state.last_alert_time > 10:
    send_alert(new_anomaly)
    st.session_state.last_alert_time = current_time


# =========================
# METRICS
# =========================
total_logs = len(filtered_logs)
errors = [l for l in filtered_logs if l["level"] == "ERROR"]
critical = [l for l in filtered_logs if l["level"] == "CRITICAL"]

col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Total Logs", total_logs)
col2.metric("❌ Errors", len(errors))
col3.metric("🔥 Critical", len(critical))
col4.metric("🚨 Anomalies", len(anomalies))


# =========================
# SYSTEM HEALTH ALERT
# =========================
if len(critical) > 20:
    st.error(f"🚨 HIGH RISK: {len(critical)} critical issues detected!")
elif len(critical) > 10:
    st.warning(f"⚠️ MEDIUM RISK: {len(critical)} issues detected")
else:
    st.success("✅ System Healthy")


# =========================
# LOG TABLE
# =========================
st.subheader("📄 Logs Table")

def highlight_errors(row):
    if row["level"] in ["ERROR", "CRITICAL"]:
        return ["background-color: red"] * len(row)
    return [""] * len(row)

if not df.empty:
    st.dataframe(df.style.apply(highlight_errors, axis=1))
else:
    st.warning("No logs available")


# =========================
# CHARTS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Logs per Service")
    if not df.empty:
        service_counts = df["service"].value_counts()
        st.bar_chart(service_counts)

with col2:
    st.subheader("📊 Severity Distribution")
    if not df.empty:
        level_counts = df["level"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(level_counts, labels=level_counts.index, autopct="%1.1f%%")
        st.pyplot(fig)


# =========================
# LIVE REFRESH
# =========================
time.sleep(1)
st.rerun()