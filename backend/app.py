from flasgger import Swagger
from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
swagger = Swagger(app)
CORS(app, origins="*", supports_credentials=True)


#static
@app.route("/")
def main_page():
    return send_from_directory('static', "index.html")


@app.route("/js/<path:path>")
def js_files(path):
    return send_from_directory('static/js', path)


@app.route("/css/<path:path>")
def css_files(path):
    return send_from_directory('static/css', path)