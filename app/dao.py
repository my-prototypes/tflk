from app.models import Usuario
from app.repository import UsuarioRepository

class UsuarioDAO:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def cadastrar_usuario(self, usuario):
        self.usuario_repository.cadastrar_usuario(usuario)

    def listar_usuarios(self):
        rows = self.usuario_repository.listar_usuarios()
        usuarios = []
        for row in rows:
            usuario = Usuario(row[1], row[2], row[3], row[4])
            usuarios.append(usuario)
        return usuarios
    
    def buscar_usuario_por_username(self, username):
        row = self.usuario_repository.buscar_usuario_por_username(username)
        if row:
            usuario = Usuario(row[1], row[2], row[3], row[4])
            return usuario
        return None