from pipeline.generator import generate_log
import time

def stream_logs():
    while True:
        yield generate_log()
        time.sleep(0.5)