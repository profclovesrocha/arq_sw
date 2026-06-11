import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_muito_segura'
    # Conexão: mysql+pymysql://usuario:senha@servidor/nome_banco
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://eco_user:eco_senha@db/ecolocaliza_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False