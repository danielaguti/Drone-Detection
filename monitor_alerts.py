import time
import os

log_path = "/home/pi/drone_alert_log.txt"
last_modified = 0
last_line = ""
clear_timeout = 10  # seconds

while True:
    try:
        if os.path.exists(log_path):
            new_modified = os.path.getmtime(log_path)
            if new_modified != last_modified:
                last_modified = new_modified
                with open(log_path, 'r') as f:
                    lines = f.readlines()
                    if lines:
                        last_line = lines[-1].strip()
                        print(f"[ALERT] {last_line}")
                        last_alert_time = time.time()
            else:
                if time.time() - last_modified > clear_timeout:
                    print("[STATUS] CLEAR - No drone detected.")
                    time.sleep(1)
        else:
            print("[INFO] Waiting for log file to appear...")
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting monitor...")
        break
    except Exception as e:
        print(f"[ERROR] {e}")
        time.sleep(1)
