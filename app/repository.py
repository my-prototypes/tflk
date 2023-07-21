import sqlite3

class UsuarioRepository:
    def __init__(self, db='usuarios.db'):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, fullname text, email text, username text, password text)''')
        self.conn.commit()

    def cadastrar_usuario(self, usuario):
        self.c.execute("SELECT * FROM usuarios WHERE email=?", (usuario.email,))
        if self.c.fetchone():
            return False
        self.c.execute("INSERT INTO usuarios VALUES (?, ?, ?, ?, ?)",
                       (None, usuario.nome, usuario.email, usuario.username, usuario.password))
        self.conn.commit()

    def listar_usuarios(self):
        self.c.execute("SELECT * FROM usuarios")
        return self.c.fetchall()
    
    def buscar_usuario_por_username(self, username):
        self.c.execute("SELECT * FROM usuarios WHERE username=?", (username,))
        return self.c.fetchone()

    def remover_usuarios(self):
        self.c.execute("DELETE FROM usuarios")
        self.conn.commit()

    # Outros métodos de manipulação de dados dos usuarios

class ImagemRepository:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db', check_same_thread=False)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS imagens (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_arquivo text, caminho_arquivo text, usuario text)''')
        self.conn.commit()

    # Lógica para cadastrar a imagem no banco de dados
    def cadastrar_imagem(self, imagem, usuario):
        self.c.execute("INSERT INTO imagens VALUES (?, ?, ?, ?)",
                       (None,imagem.nome_arquivo, imagem.caminho_arquivo, usuario))
        self.conn.commit()
    
    # Lógica para listar as imagens cadastradas    
    def listar_imagens(self):
        self.c.execute("SELECT * FROM imagens")
        return self.c.fetchall()

    # Outros métodos de manipulação de dados das imagens