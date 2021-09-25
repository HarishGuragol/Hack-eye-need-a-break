import time

from sqlalchemy import create_engine

from db.config import Config

uri = "postgresql://{login}:{password}@{db_service_name}:{port}/{database}"
uri = uri.format(**{
    "login": Config.POSTGRES_USER,
    "password": Config.POSTGRES_PASSWORD,
    "database": Config.POSTGRES_DB,
    "port": Config.POSTGRES_PORT,
    "db_service_name": Config.DB_SERVICE_NAME
})

engine = create_engine(uri)
while True:
    print("Trying to connect to the database...")
    try:
        engine.connect()
        print("Successful connection to the database!")
        break
    except:
        print("Error when connecting to the database =(")
    time.sleep(3)