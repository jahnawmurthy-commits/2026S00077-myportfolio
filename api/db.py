import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

def connect(write : bool = False):
    prefix = "DB_WRITE_" if write else  "DB_"
    user = os.getenv(prefix + "USER")
    password = os.getenv(prefix + "PASSWORD")
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT"),
        user = user,
        password = password,
        database = os.getenv("DB_NAME"),
    )
def execute(conn, sql, params = ()):
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        conn.commit()
        return cursor.rowcount, cursor.lastrowid