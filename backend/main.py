import os

from backend.app import app
from backend.api import *
from backend.utils.test_data import add_test_data
from db.migration import make_migration


def run_server():
    # add_test_data()
    if os.environ.get('PROD', False):
        print("Production server is running!")
        app.run(host="0.0.0.0", port=80)
    else:
        print("Dev server is running!")
        app.run(port=5000)


if __name__ == '__main__':
    run_server()