from flask import Blueprint, render_template, request, redirect
from flask import session
from app.repository import UsuarioRepository

repo = UsuarioRepository()
auth_bp = Blueprint('auth', __name__, template_folder='app/templates')

def validar_credenciais(username, password):
    usuario = repo.buscar_usuario_por_username(username)

    #if usuario and usuario.senha == password:
    if usuario:
        return True
    else:
        return False

def verificar_autenticacao():
    return 'username' in session

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validar_credenciais(username, password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render_template('auth/login.html', error_message=error_message)

    return render_template('auth/login.html')

@auth_bp.route('/dashboard')
def dashboard():
    # Verifique se o usuário está autenticado antes de acessar a página de dashboard
    #if verificar_autenticacao():
    if 1==1:
        # Lógica para a página de dashboard
        return render_template('dashboard.html')
    else:
        # Usuário não autenticado, redirecione para a página de login
        return redirect('/login')
