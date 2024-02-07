import subprocess

subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", '"code added"'])
subprocess.call(["git", "push"])
subprocess.call(["clear"])
print("Code Uploded")
