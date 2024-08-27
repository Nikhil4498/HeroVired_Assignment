
#CPU Usage Monitoring

import psutil
import time

def monitor_cpu_usage(threshold=80):
    print("Monitoring CPU usage...")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

monitor_cpu_usage(threshold=80)


