from flask import Flask
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
swagger = Swagger(app)
CORS(app, origins="*", supports_credentials=True)
