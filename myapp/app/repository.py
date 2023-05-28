import sqlite3

class UsuarioRepository:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (nome text, email text, senha text)''')
        self.conn.commit()

    def cadastrar_usuario(self, usuario):
        self.c.execute("INSERT INTO usuarios VALUES (?, ?, ?)",
                       (usuario.nome, usuario.email, usuario.senha))
        self.conn.commit()

    def listar_usuarios(self):
        self.c.execute("SELECT * FROM usuarios")
        return self.c.fetchall()