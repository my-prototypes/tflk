import unittest
from app.repository import UsuarioRepository
from app.tests.unit_tests.CT_TU_01 import TestUsuarioRepositoryMethods

class TestRun():
    def __init__(self):
        self.usuario_repository = UsuarioRepository(db='usuarios_test.db')
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestUsuarioRepositoryMethods(usuario_repository=self.usuario_repository))

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

# Para executar os testes, use o comando na raiz do projeto:
# python -m unittest app.tests.test_run
if __name__ == '__main__':
    TestRun().run()