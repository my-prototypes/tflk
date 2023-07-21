import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models import Usuario
from app.repository import UsuarioRepository
from app.dao import UsuarioDAO

class TestLoginFeature(unittest.TestCase):
        URL_LOGIN = "http://localhost:5000/login"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.driver = webdriver.Firefox()            
            self.driver.get(self.URL_LOGIN)
            self.username_input = self.driver.find_element(By.NAME, "username")
            self.password_input = self.driver.find_element(By.NAME, "password")
            self.login_button = self.driver.find_element(By.NAME, "btn_singin")
            self.usuario_dao = UsuarioDAO(UsuarioRepository(db='usuarios_test.db'))

        def load_user_data(self):
            self.usuario_dao.remover_usuarios()
            self.usuario_dao.cadastrar_usuario(Usuario(id=None, fullname="Armando Soares Sousa", email="armando@gmail.com", username="armando", password="armando"))

        def free_user_data(self):
            self.usuario_dao.remover_usuarios()
            self.usuario_dao.fechar_conexao()

        def setUp(self):
            self.load_user_data()
        
        def test_login_usuario_valido(self):
            self.assertIn("MyImage | Log in", self.driver.title)  # Verifica se o título da página contém "MyImage | Log in"
            # Dados de um usuario valido
            self.username_input.send_keys("armando")
            self.password_input.send_keys("armando")
            self.login_button.click()
            # Aguarda um pouco para que a página seja carregada após o login (se necessário)
            self.driver.implicitly_wait(3)
            # Verifica se a página redirecionou corretamente após o login (verifique o título ou algum elemento na página)
            self.assertIn("dashboard", self.driver.current_url)  # Substitua "PÁGINA_DE_DESTINO" pela URL da página para onde o login deve redirecionar
            assert 'armando' in self.driver.page_source

        def test_login_invalido(self):
            self.assertIn("MyImage | Log in", self.driver.title) 
            # Dados de um usuario invalido
            self.username_input.send_keys("armandos")
            self.password_input.send_keys("armandos")
            self.login_button.click()
            # Aguarda 3 segundo
            self.driver.implicitly_wait(3)
            # Verifica se continua na pagina de login
            self.assertIn("login", self.driver.current_url)
            assert 'Credenciais inválidas' in self.driver.page_source

        def tearDown(self):
            self.driver.close()
            self.driver.quit()
            self.free_user_data()

if __name__ == "__main__":
    unittest.main()