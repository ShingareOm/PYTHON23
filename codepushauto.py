import subprocess
import time

def upload():
    subprocess.call(["git", "add", "*"])
    subprocess.call(["git", "commit", "-m", '"code added"'])
    subprocess.call(["git", "push"])
    print("\033c", end='')
    print("Code Uploded")

while True:
    upload()
    time.sleep(300)