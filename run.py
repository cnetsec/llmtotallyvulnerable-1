from dotenv import load_dotenv
import os
from app import app

# LLM 004 - Proteção de Tokens e Credenciais
# Carregar variáveis de ambiente do arquivo .env
# Certifique-se de que o arquivo .env não esteja exposto publicamente (adicione .env no .gitignore).
# Nunca coloque credenciais sensíveis no código-fonte. Utilize variáveis de ambiente para gerenciar tokens, chaves secretas, etc.
load_dotenv()

if __name__ == "__main__":
    # LLM 003 - Debug em Produção
    # Obter o host e a porta de variáveis de ambiente, com fallback para valores padrão
    # **Em ambientes de produção**, nunca use debug=True, pois isso pode expor informações sensíveis de erros.
    host = os.getenv('FLASK_RUN_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_RUN_PORT', 5000))
    
    # LLM 003 - Debug em Produção
    # O modo debug nunca deve ser ativado em produção, pois pode fornecer dados sensíveis (como traceback de erros).
    debug = os.getenv('FLASK_ENV', 'development') == 'development'  # Defina como False em produção
    
    # LLM 005 - Controle de Acesso Inadequado
    # Certifique-se de que a aplicação tenha controles adequados para impedir acessos não autorizados.
    # A variável de ambiente `FLASK_RUN_HOST` deve ser configurada corretamente para permitir acessos apenas de IPs seguros (não usar 0.0.0.0 em produção sem firewall adequado).
    app.run(debug=debug, host=host, port=port)
