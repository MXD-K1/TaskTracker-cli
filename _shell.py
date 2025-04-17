"""This script is wrote for testing purposes only and not meant to be used by others.
Commands must be written directly without writing "python cli_task_tracker.py" or "task-tracker". """

import subprocess
import sys


def main():
    while True:
        try:
            task = input("> ")
            if task != "q":
                subprocess.run(f'py cli_task_tracker.py {task}', shell=True, text=True)
            else:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
