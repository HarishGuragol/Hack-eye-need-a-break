from backend.app import app
from backend.api import *
from backend.utils.test_data import add_test_data


def run_server():
    add_test_data()
    app.run(port=5000)

if __name__ == '__main__':
    run_server()