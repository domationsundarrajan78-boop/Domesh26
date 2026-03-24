import json

def parse_log(log):
    try:
        return json.loads(log)
    except:
        return None