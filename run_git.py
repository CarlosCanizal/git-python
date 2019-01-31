import subprocess
subprocess.call(["git", "add", "."])
subprocess.call(["git","commit", "-m", "Automated commit"])
subprocess.call(["git", "push", "origin", "master"])
print("Hello World")