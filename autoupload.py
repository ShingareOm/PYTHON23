import time
import subprocess

while True:
    subprocess.run(["python", "codepushauto.py"])
    time.sleep(300)  # 300 seconds = 5 minutes
