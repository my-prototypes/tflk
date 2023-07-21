from app.models import Usuario

class UsuarioDAO:
    def __init__(self, repository):
        self.usuario_repository = repository

    def cadastrar_usuario(self, usuario):
        self.usuario_repository.cadastrar_usuario(usuario)

    def listar_usuarios(self):
        rows = self.usuario_repository.listar_usuarios()
        usuarios = []
        for row in rows:
            usuario = Usuario(row[0],row[1], row[2], row[3], row[4])
            usuarios.append(usuario)
        return usuarios
    
    def buscar_usuario_por_username(self, username):
        row = self.usuario_repository.buscar_usuario_por_username(username)
        if row:
            usuario = Usuario(row[0],row[1], row[2], row[3], row[4])
            return usuario
        return None

    def remover_usuarios(self):
        self.usuario_repository.remover_usuarios()

    def fechar_conexao(self):
        self.usuario_repository.conn.close()