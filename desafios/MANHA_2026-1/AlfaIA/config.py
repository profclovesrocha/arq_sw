import os

class DevelopmentConfig:
    SECRET_KEY = "dev-secret-imip-2025"
    SQLALCHEMY_DATABASE_URI = "sqlite:///imip.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class TestingConfig:
    SECRET_KEY = "test-secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

class ProductionConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", "prod-troque-em-producao")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///imip_prod.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
