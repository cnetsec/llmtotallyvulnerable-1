import os
from flask import Flask
from app.ask import ask_blueprint
from app.train import train_blueprint
from app.model import init_db

app = Flask(__name__, template_folder='templates')
app.secret_key = os.urandom(24)

# Registrar blueprints
app.register_blueprint(ask_blueprint, url_prefix='/ask')
app.register_blueprint(train_blueprint, url_prefix='/train')

# Inicialização do banco de dados SQLite (se necessário)
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

