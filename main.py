from pipeline.ingestion import stream_logs
from pipeline.parser import parse_log
from pipeline.processor import process_log
from detection.anomaly import detect_anomaly
from detection.alert import send_alert

window = []

for raw in stream_logs():
    parsed = parse_log(raw)
    processed = process_log(parsed)

    if processed:
        window.append(processed)

    if len(window) == 100:
        print("📊 Sending report for first 100 logs...")

        anomalies = detect_anomaly(window)
        send_alert(anomalies)

        break