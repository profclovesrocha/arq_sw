class Config:

    #caminho do banco SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    #desativa avisos desnecessários
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "inserir senha com arquivo .env"