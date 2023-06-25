import unittest
from app.models import Usuario
from app.repository import UsuarioRepository

class TestUsuarioRepositoryMethods(unittest.TestCase):
    def setUp(self, usuario_repository=UsuarioRepository()):
        self.usuario_repository: UsuarioRepository = usuario_repository
        self.usuario_repository.c.execute("DELETE FROM usuarios")
        self.usuario_repository.conn.commit()
    
    def test_verificar_se_tabela_existe(self):
        self.usuario_repository.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='usuarios'")
        self.assertTrue(self.usuario_repository.c.fetchone())
    
    def test_cadastrar_usuario(self):
        usuario = Usuario('teste', 'jose@gmail.com', '123')
        self.usuario_repository.cadastrar_usuario(usuario)
        self.usuario_repository.c.execute("SELECT * FROM usuarios WHERE nome=?", (usuario.nome,))
        self.assertEqual(self.usuario_repository.c.fetchone(), ('teste', 'jose@gmail.com', '123'))

    def test_listar_usuarios(self):
        usuario1 = Usuario('teste1', 'joao@gmail.com', '123')
        usuario2 = Usuario('teste2', 'josias@outlook.com', '123')
        self.usuario_repository.cadastrar_usuario(usuario1)
        self.usuario_repository.cadastrar_usuario(usuario2)
        self.assertEqual(self.usuario_repository.listar_usuarios(), [('teste1', 'joao@gmail.com', '123'), ('teste2', 'josias@outlook.com', '123')])
    
    def test_buscar_usuario(self):
        usuario = Usuario('teste', 'jose@gmail.com', '123')
        self.usuario_repository.cadastrar_usuario(usuario)
        self.assertEqual(self.usuario_repository.buscar_usuario_por_username('teste'), ('teste', 'jose@gmail.com', '123'))
