import unittest
from app.models import Usuario
from app.repository import UsuarioRepository

class TestUsuarioRepositoryMethods(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario_repository = UsuarioRepository(db='usuarios_test.db')

    def free_user_data(self):
        self.usuario_repository.remover_usuarios()
        self.usuario_repository.conn.close()

    def procura_em_lista_tuplas(self, string_procurada, lista_de_tuplas):
        # Verifica se a string está presente em alguma posição de alguma tupla da lista
        if any(string_procurada in tupla for tupla in lista_de_tuplas):
            resultado = True
        else:
            resultado = False
        return resultado

    def setUp(self):
        self.usuario_repository.remover_usuarios()
            
    def test_cadastrar_usuario(self):
        usuario = Usuario(id=None, fullname='Teste Jose', email='jose@gmail.com',username='testexpto', password='123')
        self.usuario_repository.cadastrar_usuario(usuario)
        retorno = self.usuario_repository.buscar_usuario_por_username(usuario.username)
        id, nome_completo, e_mail, username, senha = retorno[0], retorno[1], retorno[2], retorno[3], retorno[4]
        self.assertEqual(nome_completo, 'Teste Jose')
        self.assertEqual(e_mail, 'jose@gmail.com')
        self.assertEqual(username, 'testexpto')
        self.assertEqual(senha, '123')

    def test_listar_usuarios(self):
        usuario1 = Usuario(id=None, fullname='Teste1 Joao', email='joao@gmail.com', username='teste1', password='123')
        usuario2 = Usuario(id=None, fullname='Teste2 Josias', email='josias@outlook.com', username='teste2',password='123')
        self.usuario_repository.cadastrar_usuario(usuario1)
        self.usuario_repository.cadastrar_usuario(usuario2)
        qtd_usuarios = len(self.usuario_repository.listar_usuarios())
        self.assertEqual(qtd_usuarios, 2)
        # Pega usuario, faz a busca na lista e checa se aparece na lista
        self.assertTrue(self.procura_em_lista_tuplas(usuario1.username,self.usuario_repository.listar_usuarios()))
        self.assertTrue(self.procura_em_lista_tuplas(usuario2.username,self.usuario_repository.listar_usuarios()))
    
    def tearDown(self):
        self.free_user_data()