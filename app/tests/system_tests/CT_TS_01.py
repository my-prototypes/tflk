import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from app.models import Usuario
from app.repository import UsuarioRepository

class TestLoginFeature(unittest.TestCase):
    
        def setUp(self):
            self.usuario_repository = UsuarioRepository(db='usuarios_test.db')
            self.usuario_repository.conn.execute("DELETE FROM usuarios")
            self.usuario_repository.conn.commit()
            self.usuario_repository.cadastrar_usuario(Usuario("jose", "kilo@aag.com", "123"))
            self.driver : webdriver.Chrome = webdriver.Chrome()
            self.driver.get("http://127.0.0.1:5000/")
        
        def test_login_usuario_valido(self):
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            self.driver.find_element(By.ID, "username").send_keys("jose")
            self.driver.find_element(By.ID, "password").send_keys("123")
            self.driver.find_element(By.XPATH, "/html/body/form/input[3]").click()
            assert self.driver.title == "Dashboard"

        def test_login_usuario_invalido(self):
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            self.driver.find_element(By.ID, "username").send_keys("ffff")
            self.driver.find_element(By.ID, "password").send_keys("4122")
            self.driver.find_element(By.XPATH, "/html/body/form/input[3]").click()
            assert self.driver.title == "Login"
        
        def test_login_usuario_valido_sem_senha(self):
            self.driver.find_element(By.LINK_TEXT, "Login").click()
            self.driver.find_element(By.ID, "username").send_keys("jose")
            self.driver.find_element(By.XPATH, "/html/body/form/input[3]").click()
            assert self.driver.title == "Login"

        def tearDown(self):
            self.driver.quit()
            self.usuario_repository.conn.execute("DELETE FROM usuarios")
            self.usuario_repository.conn.commit()
            self.usuario_repository.conn.close()

if __name__ == "__main__":
    unittest.main()
