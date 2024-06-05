# config.py

import secrets
class Config:
    SECRET_KEY = secrets.token_urlsafe(32)  # ou defina a chave diretamente aqui
    DEBUG = True  # Defina como False em um ambiente de produção
    # Outras configurações...

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Use um banco de dados apropriado para produção

class ProductionConfig(Config):
    DEBUG = False
    # Configurações específicas de produção...
