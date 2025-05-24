# Definir a imagem base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do repositório para o container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação (ajuste conforme necessário para o seu projeto)
CMD ["python", "app.py"]

# Ou o comando equivalente para o seu projeto, dependendo da configuração
