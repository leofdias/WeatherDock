# Usa uma imagem oficial do Python como imagem de base
FROM python:3.8-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos primeiro, para aproveitar o cache da camada Docker
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o resto do código da aplicação
COPY . .

# Expõe a porta que o Flask vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
