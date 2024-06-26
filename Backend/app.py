from flask import Flask
from flask_cors import CORS

from router.test import test
from router.api import api
from router.error import not_found, server_error

# Loading .env file
from config_env import config_env

# ! == About ==
# In charge of running server and store Flask App

app = Flask(__name__)
CORS(app)

# Add routes
app.register_blueprint(test)
app.register_blueprint(api)
app.register_error_handler(404, not_found)
app.register_error_handler(503, server_error)

if __name__ == '__main__':
    print("[SERVER] Running Server --> localhost:3030")
    app.run(host="localhost", port=3030, debug=config_env.get("FLASK_DEBUG"))
