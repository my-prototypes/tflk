from flask import Blueprint, render_template, request, redirect
from flask import session
from app.repository import UsuarioRepository
from app.models import Usuario
from app.dao import UsuarioDAO

dashboard_bp = Blueprint('dashboard', __name__, template_folder='app/templates')
repository = UsuarioRepository()
usuario_dao = UsuarioDAO(repository)

def verificar_autenticacao():
    return 'username' in session

@dashboard_bp.route('/dashboard')
def painel_principal():
    # Verifique se o usuário está autenticado antes de acessar a página de dashboard
    if verificar_autenticacao():
        usuarios = []
        quantidade_usuarios = len(usuarios)
        imagens = []
        quantidade_imagens = len(imagens)

        return render_template("dashboard/starter.html", usuario = session['username'], 
                profilePic="", titulo="Dashboard", usuarios = usuarios, 
                imagens = imagens, quantidade_usuarios=quantidade_usuarios, quantidade_imagens=quantidade_imagens) 
    else:
        # Usuário não autenticado, redirecione para a página de login
        return redirect('/login')

"""Show the user profile """
@dashboard_bp.route("/profile")
def profile():
    usuario = usuario_dao.buscar_usuario_por_username(username=session['username'])
    return render_template("dashboard/profile.html", usuario = session['username'], 
            profilePic="", titulo="Profile", nome=usuario.nome, id=str(usuario.id), email=usuario.email)