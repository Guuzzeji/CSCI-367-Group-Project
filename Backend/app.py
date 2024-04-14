from flask import Flask

from router.test import test
from router.api import api

# Loading .env file
from config_env import config_env

app = Flask(__name__)
app.register_blueprint(test)
app.register_blueprint(api)

if __name__ == '__main__':
    print("Running Server --> "
          + "localhost:"
          + "3030")
    app.run(host="localhost", port=3030, debug=True)
