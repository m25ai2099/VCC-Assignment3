import psutil
import time
import os

THRESHOLD = 75

def trigger_scaling():
    print("⚠️ Threshold exceeded! Triggering scaling...")
    os.system("bash ../autoscaling/trigger_scale.sh")

while True:
    cpu = psutil.cpu_percent(interval=2)
    memory = psutil.virtual_memory().percent

    print(f"CPU: {cpu}% | Memory: {memory}%")

    if cpu > THRESHOLD or memory > THRESHOLD:
        trigger_scaling()
        break

    time.sleep(3)
