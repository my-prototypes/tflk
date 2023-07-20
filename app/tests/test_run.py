import unittest
from app.tests.system_tests.CT_TS_01 import TestLoginFeature

class TestRun():
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite.addTest(TestLoginFeature())

    def run(self):
        runner = unittest.TextTestRunner()
        runner.run(self.suite)

# Para executar os testes, use o comando na raiz do projeto:
# python -m unittest app.tests.test_run
if __name__ == '__main__':
    TestRun().run()