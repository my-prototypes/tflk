from flask import Blueprint, request, redirect, render_template
from app.models import Usuario
from app.repository import UsuarioRepository
from app.utils.utilidades import Constant
from flask import flash
from flask import url_for
from flask import session

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
        id = 1
        nome = request.form['nome']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        usuario = Usuario(id, nome, email, username, password)
        repo.cadastrar_usuario(usuario)
        return redirect('/listar')
    return render_template('usuarios/cadastrar_usuario.html')

@usuarios_bp.route("/<int:id>/update", methods=["GET", "POST"])
def update(id):    
    if request.method == "POST":
        username = request.form["username"]
        file_name_to_store = "picture-" + str(id) + ".png" 
        error = None

        if not username:
            error = "Username is required."

        if error is not None:
            flash(error)
        else:
            ##db = get_db()
            ##db.execute("UPDATE user SET image = ? WHERE id = ?", (file_name_to_store, id))
            try:
                # Processa o upload do arquivo de imagem
                print('Processamento do upload da imagem')
                # TO DO: isolar o tratamento de arquivo
                file_image = request.files["image"]
                path_to_save = Constant.PATH_UPLOADS + "/" + file_name_to_store
                # Salva o arquivo no diretorio de uploads
                file_image.save(path_to_save)
            except:
                error_processing_upload = "Erro no processamento do upload do processamento da imagem."
                if error_processing_upload is not None:
                    flash(error_processing_upload, 'danger')
                    return redirect(url_for("usuario.listar_usuarios"))
            message = "Usuario atualizado com sucesso!"
            flash(message, 'success')
            return redirect(url_for("dashboard.profile"))

    resultado = repo.buscar_usuario_por_username(username=session['username'])
    print(resultado)
    usuario = Usuario(id=resultado[0], fullname=resultado[1], email=resultado[2], username=resultado[3], password=resultado[4])    

    return render_template("usuarios/imagem.html", usuario = session['username'], 
            profilePic="", titulo="Update image", usuario_logado=session['username'], nome=usuario.username)