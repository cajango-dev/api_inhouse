import subprocess
import webbrowser
import time
import sys
import os

venv_python = os.path.join("venv", "Scripts", "python.exe")

url = "http://127.0.0.1:8000/admin/login/?next=/admin/"

server = subprocess.Popen([venv_python, "manage.py", "runserver"])

time.sleep(3)

webbrowser.open(url)

server.wait()
