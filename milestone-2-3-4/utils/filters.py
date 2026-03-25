def filter_logs(logs, services, levels):
    return [
        log for log in logs
        if (not services or log["service"] in services)
        and (not levels or log["level"] in levels)
    ]