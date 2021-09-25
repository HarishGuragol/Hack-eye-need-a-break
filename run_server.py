from backend.main import run_server
from db.migration import make_migration

make_migration()
run_server()