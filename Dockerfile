# Usa uma imagem base do Python oficial, versão 3.11
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o container
# Isso permite que o Docker use o cache para não reinstalar dependências
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Adiciona o Netcat para o script entrypoint.sh funcionar
RUN apt-get update && apt-get install -y netcat-traditional

# Copia o script de entrada para esperar pelo banco de dados
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

# Torna o script executável
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copia todo o código do projeto para o container
COPY . .

# Expõe a porta que o Django usará
EXPOSE 8000

# Define o ponto de entrada do container para o script.
# Agora, toda vez que o container web for iniciado, ele rodará esse script primeiro.
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Define o comando padrão para iniciar a aplicação, que será executado pelo entrypoint.sh
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]