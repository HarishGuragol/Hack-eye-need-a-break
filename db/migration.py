from db.engine import engine
from db.meta import metadata
from db.models import *


def make_migration():
    print("Migrations is starting...")
    metadata.create_all(engine)
    print("Migrations are applied!")


if __name__ == '__main__':
    make_migration()

