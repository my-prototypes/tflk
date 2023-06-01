from flask import Blueprint, request, redirect, render_template
from app.models import Usuario
from app.repository import UsuarioRepository

# Create a Blueprint object for the users blueprint
usuarios_bp = Blueprint('usuarios', __name__, template_folder='app/templates')
repo = UsuarioRepository()

@usuarios_bp.route('/listar')
def listar_usuarios():
    usuarios = repo.listar_usuarios()
    return render_template('usuarios/listar_usuarios.html', usuarios=usuarios)

@usuarios_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        usuario = Usuario(nome, email, senha)
        repo.cadastrar_usuario(usuario)
        return redirect('/listar')
    return render_template('usuarios/cadastrar_usuario.html')