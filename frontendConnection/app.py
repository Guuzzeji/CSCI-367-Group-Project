from flask import Flask

from test import test
from api import api
from error import not_found, server_error

# Loading .env file
from config_env import config_env
from flask_cors import CORS
# ! == About ==
# In charge of running server and store Flask App

app = Flask(__name__)
app.register_blueprint(test)
app.register_blueprint(api)
app.register_error_handler(404, not_found)
app.register_error_handler(503, server_error)
CORS(app)
if __name__ == '__main__':
    print("[SERVER] Running Server --> localhost:3030")
    app.run(host="localhost", port=3030, debug=config_env.get("FLASK_DEBUG"))
