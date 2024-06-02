# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação para o diretório de trabalho
COPY . .

# Expor a porta que a aplicação vai rodar
EXPOSE 5000

# Inicializar o banco de dados
RUN python -c 'from app.model import init_db; init_db()'

# Comando para rodar a aplicação
CMD ["python", "run.py"]

