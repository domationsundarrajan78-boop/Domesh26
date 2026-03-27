from detection.alert import send_alert

test_data = [{"level": "ERROR", "service": "test", "status": 999}]

send_alert(test_data)