# 1. Usa uma imagem oficial leve do Python
FROM python:3.11-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /app

# 3. Define variáveis de ambiente para o Python
# Impede que o Python escreva arquivos .pyc no disco
ENV PYTHONDONTWRITEBYTECODE=1
# Garante que as saídas do log apareçam imediatamente no terminal
ENV PYTHONUNBUFFERED=1

# 4. Copia o arquivo de dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt /app/

# 5. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia o restante do código do projeto para o container
COPY . /app/

# 7. Informa a porta que o container vai expor
EXPOSE 5000

# 8. Comando para rodar a aplicação escutando em todas as interfaces de rede (0.0.0.0)
CMD ["python", "app.py"]