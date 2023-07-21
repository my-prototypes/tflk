import unittest
from app.tests.unit_tests.CT_TU_01 import TestUsuarioRepositoryMethods

class TestRun():
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestUsuarioRepositoryMethods())

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

# Para executar os testes, use o comando na raiz do projeto:
# python -m unittest app.tests.test_run
if __name__ == '__main__':
    TestRun().run()