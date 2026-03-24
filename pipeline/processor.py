def process_log(log):
    if log is None:
        return None

    return {
        "timestamp": log.get("timestamp"),
        "level": log.get("level"),
        "service": log.get("service"),
        "status": log.get("status"),
        "message": log.get("message")
    }