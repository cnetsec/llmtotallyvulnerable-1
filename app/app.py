import os
from flask import Flask
from app.ask import ask_blueprint
from app.train import train_blueprint

app = Flask(__name__, template_folder='app/templates')

# LLM 001 - A Chave Secreta (app.secret_key) sendo gerada com os.urandom(24)
# Isso pode ser vulnerável a ataques se a chave for previsível ou compartilhada em ambiente de produção.
# Uma recomendação é usar um mecanismo de gestão de chaves adequadas ou armazenar a chave em uma variável de ambiente.
app.secret_key = os.urandom(24)  # Chave secreta para a sessão

# LLM 002 - Inicialização do Banco de Dados
# A inicialização do banco de dados em um contexto sem validações adequadas pode levar a injeções de SQL ou falhas de segurança
# Se o banco de dados estiver mal configurado, ele pode expor informações sensíveis. Certifique-se de usar boas práticas de segurança no banco.
from app import model
model.init_db()

# LLM 003 - Execução de Flask com `debug=True` em produção
# Manter o debug ativado pode ser perigoso em ambientes de produção, pois ele pode fornecer informações sensíveis de erro.
# A recomendação é usar `debug=False` em produção para evitar a exposição de detalhes internos.
if __name__ == "__main__":
    app.run(debug=True)  # LLM 003 - Em produção, debug=True deve ser desativado

# LLM 007 - Proteção Contra XSS (Cross-Site Scripting)
# A aplicação parece estar lidando com entradas de usuário, o que pode ser uma porta de entrada para **ataques XSS**.
# Certifique-se de escapar qualquer dado de usuário inserido em páginas HTML ou em resposta ao front-end.
# Flask tem proteção embutida para evitar XSS, mas vale a pena revisar se não está expondo dados sem escapa-los corretamente.
# Se for necessário aceitar HTML de entrada do usuário, use bibliotecas de **sanitização** para garantir que não haja injeções de scripts.
