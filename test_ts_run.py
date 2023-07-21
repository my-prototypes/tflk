import subprocess
import time
import unittest

from app.tests.system_tests.CT_TS_01 import TestLoginFeature

# Função para iniciar a aplicação Flask
def start_flask_app():
    process = subprocess.Popen(["flask", "run", "--host=0.0.0.0", "--port=5000"])
    time.sleep(3) 
    return process

# Função para encerrar a aplicação Flask
def stop_flask_app(process):
    process.terminate()

if __name__ == "__main__":
    try:
        print('Carrega a aplicação')
        app_process = start_flask_app()
        print('Executa os testes automáticos do Selenium')
        unittest.main()

    finally:
        # Encerra a aplicação Flask ao final do teste
        stop_flask_app(app_process)