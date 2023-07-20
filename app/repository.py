import sqlite3

class UsuarioRepository:
    def __init__(self, db='usuarios.db'):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (nome text, email text, senha text)''')
        self.conn.commit()

    def cadastrar_usuario(self, usuario):
        self.c.execute("SELECT * FROM usuarios WHERE email=?", (usuario.email,))
        if self.c.fetchone():
            return False
        self.c.execute("INSERT INTO usuarios VALUES (?, ?, ?)",
                       (usuario.nome, usuario.email, usuario.senha))
        self.conn.commit()

    def listar_usuarios(self):
        self.c.execute("SELECT * FROM usuarios")
        return self.c.fetchall()
    
    def buscar_usuario_por_username(self, username):
        self.c.execute("SELECT * FROM usuarios WHERE nome=?", (username,))
        return self.c.fetchone()

class ImagemRepository:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS imagens
                            (nome text, caminho text, usuario text)''')
        self.conn.commit()

    # Lógica para cadastrar a imagem no banco de dados
    def cadastrar_imagem(self, imagem, usuario):
        self.c.execute("INSERT INTO imagens VALUES (?, ?, ?)",
                       (imagem.nome_arquivo, imagem.caminho_arquivo, usuario))
        self.conn.commit()
    
    # Lógica para listar as imagens cadastradas    
    def listar_imagens(self):
        self.c.execute("SELECT * FROM imagens")
        return self.c.fetchall()

    # Outros métodos de manipulação de dados das imagens