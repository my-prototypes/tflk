class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Imagem:
    def __init__(self, nome_arquivo, caminho_arquivo, usuario):
        self.nome_arquivo = nome_arquivo
        self.caminho_arquivo = caminho_arquivo
        self.usuario = usuario