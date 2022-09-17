import psycopg2 as ps



def conexion():
    try :
        con = ps.connect(
            dbname="paginas",
            user="postgres",
            password="postgres",
            host="postgres",
            port=5432
        )
        return con
    except:
        print("No pudo realizarse conexión con la datab")
