import os
import sys
# from dotenv import load_dotenv

# ! == About ==
# In charge of loading .env file and converting it into a dictionary that can be used to look up variables

# ! For easy of use, just hard coding everything
config_env = {
    "MYSQL_USERNAME": "root",
    "MYSQL_PASSWORD": "rootpassword",
    "MYSQL_HOST": "localhost",
    "MYSQL_DATABASE": "manga_db",
    "MYSQL_PORT": 4040,
    "FLASK_DEBUG": True,
}


# is_load_env = load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# if not is_load_env:
#     print("[ERROR] .env file does not exist. Please create .env file at root of backend in order to use MYSQL. .env cannot be empty either")
#     sys.exit(1)

# FLASK_DEBUG = False
# if os.getenv("FLASK_DEBUG").lower() == "true":
#     FLASK_DEBUG = True

# config_env = {
#     "MYSQL_USERNAME": os.getenv('MYSQL_USERNAME'),
#     "MYSQL_PASSWORD":  os.getenv('MYSQL_PASSWORD'),
#     "MYSQL_HOST": os.getenv('MYSQL_HOST'),
#     "MYSQL_DATABASE": os.getenv('MYSQL_DATABASE'),
#     "MYSQL_PORT": os.getenv('MYSQL_PORT'),
#     "FLASK_DEBUG": FLASK_DEBUG
# }


