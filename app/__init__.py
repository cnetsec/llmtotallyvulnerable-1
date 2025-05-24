import os
from flask import Flask
from app.ask import ask_blueprint
from app.train import train_blueprint
from app.model import init_db

app = Flask(__name__, template_folder='templates')

# LLM 001 - Chave Secreta Gerada com os.urandom(24)
# A chave secreta para a sessão é gerada de forma aleatória usando `os.urandom(24)`.
# Embora o `os.urandom()` seja adequado para gerar uma chave secreta, em um ambiente de produção, é recomendado
# usar um serviço de gerenciamento de chaves ou armazenar essa chave em uma variável de ambiente
# para evitar que ela seja exposta ou reutilizada indevidamente.
app.secret_key = os.urandom(24)

# Registrar blueprints
app.register_blueprint(ask_blueprint, url_prefix='/ask')
app.register_blueprint(train_blueprint, url_prefix='/train')

# LLM 002 - Inicialização do Banco de Dados (Proteção contra Injeções SQL)
# Ao inicializar o banco de dados com `init_db()`, é importante garantir que o código de inicialização
# esteja livre de vulnerabilidades, como **injeção SQL**. Certifique-se de usar consultas parametrizadas e
# ORMs (como SQLAlchemy) para evitar que entradas de usuários possam modificar a consulta SQL de forma maliciosa.
with app.app_context():
    init_db()

# LLM 003 - Execução de Flask com `debug=True` em produção
# Manter o debug ativado (`debug=True`) pode ser perigoso em produção, pois ele pode expor informações sensíveis
# (como detalhes de erros e stack traces) aos usuários mal-intencionados.
# **Nunca use debug=True em produção**. Defina `debug=False` quando a aplicação estiver em produção.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

    # LLM 005 - Controle de Acesso Inadequado
    # Configurar o host para `0.0.0.0` faz com que a aplicação fique acessível de qualquer IP, o que pode ser uma
    # preocupação de segurança, pois não há restrições sobre de onde a aplicação pode ser acessada.
    # Em produção, você deve restringir o acesso ao servidor a IPs conhecidos ou usar um firewall para garantir
    # que apenas clientes autorizados possam acessar o serviço.
