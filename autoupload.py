import time
import subprocess

while True:
    # Execute your file or command here
    subprocess.run(["python", "codepushauto.py"])
    
    # Wait for 5 minutes
    time.sleep(300)  # 300 seconds = 5 minutes
