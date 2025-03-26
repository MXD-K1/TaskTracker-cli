import subprocess
import sys

while True:
    task = input("> ")
    if task != "q":
        result = subprocess.run(f'python main.py {task}', shell=True, text=True)
    else:
        sys.exit()