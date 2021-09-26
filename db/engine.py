import os
import time

from sqlalchemy import create_engine

from db.config import Config


uri = "sqlite:///{current_path}/db.sqlite"
uri = uri.format(**{
    "current_path": os.path.dirname(os.path.realpath(__file__)),
})

print("uri: ", uri)

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