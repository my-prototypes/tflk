from flask import Flask, render_template
from app.controllers.auth import auth_bp
from app.controllers.dashboard import dashboard_bp
from app.controllers.usuarios import usuarios_bp
from app.controllers.imagens import imagens_bp
import os

app = Flask(__name__, template_folder='app/templates')
app.secret_key = os.environ['MY_SECRET_KEY']
app.static_folder = 'app/static'

# Register the blueprint with your application
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(imagens_bp)

@app.route('/')
def home():
    print('Carrega home.html')
    return render_template('home.html')

@app.route('/testes')
def testes():
    print('Carrega testes.html')
    return render_template('testes.html')

if __name__ == '__main__':
    app.run()