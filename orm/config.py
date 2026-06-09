import os

# Cadena de conexión a la base de datos
cadena_base_datos = "sqlite:///./database.db"

class Config:
    """Clase de configuración para la aplicación"""
    SQLALCHEMY_DATABASE_URL = cadena_base_datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "admin"
    DEBUG = True