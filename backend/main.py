import os

from backend.app import app
from backend.api import *
from backend.utils.test_data import add_test_data
from db.migration import make_migration


def run_server():
    # add_test_data()
    if os.environ.get('PROD', False):
        print("Production server is running!")
        context = ('./backend/keys/host.cert', './backend/keys/host.key')
        app.run(host="0.0.0.0", port=80, ssl_context=context)
    else:
        print("Dev server is running!")
        app.run(port=5000, debug=True)


if __name__ == '__main__':
    run_server()