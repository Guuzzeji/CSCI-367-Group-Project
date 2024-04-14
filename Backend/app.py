from flask import Flask

from router.test import test
from router.api import api

# Loading .env file
from config_env import config_env

app = Flask(__name__)
app.register_blueprint(test)
app.register_blueprint(api)

@app.errorhandler(404)
def not_found(e):
      return {
            "status": 404,
            "error": "page does not exist"
      }

@app.errorhandler(503)
def server_error(e):
      return {
            "status": 503,
            "error": "server issues :("
      }

if __name__ == '__main__':
    print("Running Server --> "
          + "localhost:"
          + "3030")
    app.run(host="localhost", port=3030, debug=True)
