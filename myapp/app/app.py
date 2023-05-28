from flask import Flask, render_template, request, redirect
from models import Usuario
from repository import UsuarioRepository

app = Flask(__name__)
repo = UsuarioRepository()

@app.route('/')
def index():
    print('Carrega index.html')
    return render_template('index.html')

@app.route('/listar')
def listar_usuarios():
    usuarios = repo.listar_usuarios()
    return render_template('listar_usuarios.html', usuarios=usuarios)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario(nome, email, senha)
        repo.cadastrar_usuario(usuario)
        return redirect('/listar')
    return render_template('cadastrar_usuario.html')

if __name__ == '__main__':
    app.run()