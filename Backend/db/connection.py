import mysql.connector
import atexit 
import sys

from config_env import config_env

# ! == About ==
# Handle connection between web server and MySQL database and allow other module to use connection const

# Creating connection
CONNECTION_TO_DB = None
try:
    CONNECTION_TO_DB = mysql.connector.connect(
        host=config_env.get("MYSQL_HOST"),
        user=config_env.get("MYSQL_USERNAME"),
        password=config_env.get("MYSQL_PASSWORD"),
        database=config_env.get("MYSQL_DATABASE"),
        port=config_env.get("MYSQL_PORT")
    )
except mysql.connector.Error as err:
    print("[ERROR] " + str(err))
    sys.exit(1)

if CONNECTION_TO_DB is None:
    print("[ERROR] Failed to connect to db for some reason")
    sys.exit(1)

# ! Doing this to end connection with db server turn off
@atexit.register
def close_db_connection_handle():
    print("[DB] Killing db connection...")
    CONNECTION_TO_DB.close()
