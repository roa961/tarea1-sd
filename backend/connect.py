from psycopg2 import *
from environs import *


con = None
cur = None

def conexion():
    try :
        con = connect(
            dbname= E
        )