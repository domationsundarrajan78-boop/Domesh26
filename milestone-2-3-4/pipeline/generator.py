import random
import time
import json

levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
services = ["auth", "payment", "db", "api"]

def generate_log():
    # 90% normal, 10% anomaly
    if random.random() < 0.5:
        level = random.choice(["INFO", "WARNING"])
        status = random.randint(200, 399)
    else:
        level = random.choice(["ERROR", "CRITICAL"])
        status = random.randint(900, 999)

    log = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "level": level,
        "service": random.choice(services),
        "status": status,
        "message": "Sample log"
    }

    return json.dumps(log)