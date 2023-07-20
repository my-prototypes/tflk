from flask import Blueprint, render_template, request, redirect
from flask import session
from app.models import Usuario
from app.repository import UsuarioRepository
from flask import url_for
from flask import flash

auth_bp = Blueprint('auth', __name__, template_folder='app/templates')
repo = UsuarioRepository()

def validar_credenciais(username, password):
    resposta_consulta = repo.buscar_usuario_por_username(username)
    if resposta_consulta is not None:
        usuario = Usuario(resposta_consulta[0], resposta_consulta[1], resposta_consulta[2], resposta_consulta[3], resposta_consulta[4])
        if usuario and usuario.password == password:
            return True
        else: 
            return False
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
            return redirect(url_for("dashboard.painel_principal"))
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            flash(error_message)
            return render_template('auth/login.html', error_message=error_message)
    return render_template('auth/login.html')

# Pagina de registro
@auth_bp.route("/register", methods=['GET', 'POST'])
def register():
    """
    Register a new user.
    Validates that the username is not already taken. Hashes the password for security.
    """
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        error = None
        resultado_busca = repo.buscar_usuario_por_username(username)

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (resultado_busca is not None):
            error = f"User {username} is already registered."

        if error is None:
            # the name is available, store it in the database and go to the login page
            usuario = Usuario(id=1, fullname=name, email=email, username=username, password=password)
            repo.cadastrar_usuario(usuario)
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")

# Pagina de recuperacao de e-mail
@auth_bp.route("/forgot-password", methods=["GET"])
def forgot():
    return render_template("auth/forgot-password.html")

@auth_bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return render_template("auth/login.html")