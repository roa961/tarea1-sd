import psycopg2 as ps
from environs import Env


def conexion():
    try :
        con = ps.connect(
            dbname=Env('POSTGRES_DB'),
            user=Env('POSTGRES_USER'),
           assword=Env('POSTGRES_PASSWORD'),
            host=Env('POSTGRES_HOST')
        )
        return con
    except:
        print("No pudo realizarse conexión con la db")
