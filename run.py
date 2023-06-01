from flask import Flask, render_template
from app.controllers.usuarios import usuarios_bp
from app.controllers.auth import auth_bp

app = Flask(__name__, template_folder='app/templates')
app.secret_key = 's3cr3tK3y!@#'

# Register the blueprint with your application
app.register_blueprint(usuarios_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    print('Carrega index.html')
    return render_template('home.html')

if __name__ == '__main__':
    app.run()