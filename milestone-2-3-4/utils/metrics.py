def calculate_metrics(logs):
    total = len(logs)
    errors = [l for l in logs if l["level"] == "ERROR"]
    critical = [l for l in logs if l["level"] == "CRITICAL"]

    return {
        "total": total,
        "errors": len(errors),
        "critical": len(critical),
        "anomalies": len(errors) + len(critical)
    }