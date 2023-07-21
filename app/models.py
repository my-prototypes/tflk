class Usuario:
    def __init__(self,id, fullname, email, username, password):
        self.id = id
        self.nome = fullname
        self.email = email
        self.username = username
        self.password = password

class Imagem:
    def __init__(self, id, nome_arquivo, caminho_arquivo, usuario):
        self.id = id
        self.nome_arquivo = nome_arquivo
        self.caminho_arquivo = caminho_arquivo
        self.usuario = usuario