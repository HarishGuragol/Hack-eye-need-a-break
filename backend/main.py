from backend.app import app
from backend.api import *
from backend.utils.test_data import add_test_data

add_test_data()
app.run(host="0.0.0.0", port=80)
