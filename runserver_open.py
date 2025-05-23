import subprocess
import webbrowser
import time
import sys
import os

# Ajuste aqui o caminho do python dentro do seu venv
# Exemplo típico no Windows:
venv_python = os.path.join("venv", "Scripts", "python.exe")

# URL para abrir
url = "http://127.0.0.1:8000/admin/login/?next=/admin/"

# Inicia o servidor Django usando o python do venv
server = subprocess.Popen([venv_python, "manage.py", "runserver"])

# Espera o servidor subir (pode ajustar o tempo, dependendo da máquina)
time.sleep(3)

# Abre o navegador na URL desejada
webbrowser.open(url)

# Aguarda o servidor rodar até ser interrompido (Ctrl+C)
server.wait()
