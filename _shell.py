# add description to tell other that this is for testing only not to be used by them

import subprocess
import sys


def main():
    while True:
        try:
            task = input("> ")
            if task != "q":
                subprocess.run(f'py main.py {task}', shell=True, text=True)
            else:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
