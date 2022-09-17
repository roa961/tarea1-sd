import psycopg2 as ps
from environs import Env


def conexion():
    try :
        env = Env()
        con = ps.connect(
            dbname="paginas",
            user="postgres",
            password="postgres",
            host="172.20.1.2",
            port=5432
        )
        return con
    except:
        print("No pudo realizarse conexión con la datab")
