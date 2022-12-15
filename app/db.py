import json
import mysql.connector
# from mysql.connector import errorcode

def get_db_config(filepath):
    f = open(filepath, "r")
    config = json.load(f)
    f.close
    return config

def db_connect(config):
    try:
        # recupération infos db
        db = mysql.connector.connect(**config)

        return db

    # except errorcode as e:
    #     print(e)

    except Exception as e:
        print(e)

    # finally:
    #     if db.is_connected():
    #         print(db.get_server_info)
