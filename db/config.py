import os


class Config:
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "docker")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "docker")
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "docker")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "2345")
    DB_SERVICE_NAME = os.environ.get("DB_SERVICE_NAME", "localhost")
