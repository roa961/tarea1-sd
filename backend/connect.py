from psycopg2 import connect
from environs import env


def conexion():
    try :
        con = connect(
            dbname=env('POSTGRES_DB'),
            user=env('POSTGRES_USER'),
           assword=env('POSTGRES_PASSWORD'),
            host=env('POSTGRES_HOST')
        )
        return con
    except:
        print("No pudo realizarse conexión con la db")