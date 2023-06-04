from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os
from app.repository import ImagemRepository
from app.models import Imagem
from flask import session

# Create a Blueprint object for the upload blueprint
imagens_bp = Blueprint('imagens', __name__, template_folder='app/templates')

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@imagens_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado no formulário
        if 'file' not in request.files:
            return render_template('imagem/upload/error.html', message='Nenhum arquivo enviado')
        
        file = request.files['file']
        
        # Verifica se um arquivo válido foi enviado
        if file.filename == '':
            return render_template('imagem/upload/error.html', message='Nenhum arquivo selecionado')
        
        if file and allowed_file(file.filename):
            # Acessar o nome do usuário armazenado na sessão username  
            current_user = session.get('username')

            filename = secure_filename(file.filename)
            
            # Salva o arquivo no diretório de upload
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            
            # Crie a instância da classe Imagem e salve as informações no banco de dados
            # Crie a instância da classe ImagemRepository para manipular os dados das imagens
            imagem = Imagem(nome_arquivo=filename, caminho_arquivo=os.path.join(UPLOAD_FOLDER, filename), usuario=current_user)
            imagem_repo = ImagemRepository()            
            # Salva a imagem no banco de dados
            imagem_repo.cadastrar_imagem(imagem, current_user)
            
            return render_template('imagem/upload/success.html', message='Upload de imagem concluído')
        else:
            return render_template('imagem/upload/error.html', message='Tipo de arquivo não suportado')
    
    return render_template('imagem/upload/upload.html')

@imagens_bp.route('/imagens', methods=['GET'])
def listar_imagens():
    # Crie uma instância da classe ImagemRepository
    imagem_repo = ImagemRepository()

    # Obtenha a lista de imagens cadastradas
    imagens = imagem_repo.listar_imagens()

    # Renderize o template com a lista de imagens
    return render_template('imagem/listagem.html', imagens=imagens)