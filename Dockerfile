# Usando uma imagem base de Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do repositório para o container
COPY . /app

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta 5000
EXPOSE 5000

# Comando para rodar a aplicação, usando o script run.py para iniciar o servidor
CMD ["python", "run.py"]
