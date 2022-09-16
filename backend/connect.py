import psycopg2 
from environs import *
from dotenv import load_dotenv
import os

con = None
cur = None

def conexion():

    load_dotenv()
    db = os.getenv("POSTGRES_DB")
    us = os.getenv("POSTGRES_USER")
    passw = os.getenv("POSTGRES_PASSWORD") 
    ht = os.getenv("POSTGRES_HOST")

    conn = psycopg2.connect(
        database= db,
        user = us,
        password = passw,
        host = ht
    )
    return conn