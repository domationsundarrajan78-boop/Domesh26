import statistics

def detect_anomaly(logs):
    if len(logs) < 10:
        return []

    anomalies = []

    # Signal 1: Level-based
    for log in logs:
        if log["level"] in ["ERROR", "CRITICAL"]:
            anomalies.append(log)

    # Signal 2: Status code z-score
    statuses = [log["status"] for log in logs]
    mean = statistics.mean(statuses)
    stdev = statistics.stdev(statuses) if len(statuses) > 1 else 1

    for log in logs:
        z_score = (log["status"] - mean) / stdev
        if abs(z_score) > 2:
            log["z_score"] = round(z_score, 2)
            anomalies.append(log)

    return anomalies