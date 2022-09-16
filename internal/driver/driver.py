import psycopg2
import sys
from decouple import config

# connect DB connects to the DB


def connect_DB():
    try:
        conn = psycopg2.connect(config("DSN"))
        print("Connected to the DB")
        return conn
    except Exception as err:
        print("cannot connect to the DB", err)
        sys.exit()
