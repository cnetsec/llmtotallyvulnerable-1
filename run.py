from dotenv import load_dotenv
import os
from app import app

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

if __name__ == "__main__":
    # Obter o host e a porta de variáveis de ambiente, com fallback para valores padrão
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    
    # Obter o modo de debug da variável de ambiente
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    app.run(debug=debug, host=host, port=port)
