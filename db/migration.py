from db.engine import engine
from db.meta import metadata
from db.models import *

print("Migrations is starting...")
metadata.create_all(engine)
print("Migrations are applied!")
