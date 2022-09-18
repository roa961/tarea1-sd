from operator import ifloordiv
import requests
from bs4 import BeautifulSoup
import csv
import psycopg2
import os
from dotenv import load_dotenv
import limpieza
import ip
import time as t

t.sleep(15)

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
cur = conn.cursor()
cur.execute("select * from information_schema.tables where table_name=%s", ('webs',))
val = bool(cur.rowcount)
if val:
    print("Tabla ya existente")
else:
    cur.execute("create table webs(id int, title text, description text, keywords text, URL text); ")
    cur.execute("commit;")
    print("Tabla 'webs' creada")

with open("paginas.txt", 'r') as file:
    rf = csv.reader(file, delimiter='\t')
    limit = 100
    cont = 0
    next(rf)
    for fila in rf:
        if cont == limit:
            break
        try: 
            page = requests.get(fila[4],timeout=1)
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, 'html.parser')
            else:
                continue
            
            if soup.find("meta", {"name":"description"}):
                body = soup.find("meta", {"name":"description"})["content"]
            else:
                continue

            if soup.find("meta",{"name":"title"}):
                title = soup.find("meta",{"name":"title"})["content"]
            elif soup.find_all('title'):
                title = soup.find('title').text
            else:
                continue
                
            if soup.find("meta", {"name":"keywords"}):
                keywords = soup.find("meta", {"name":"keywords"})["content"]
            else:
                continue
            cur.execute("insert into webs(id, title, description, keywords, url ) values(%s,%s,%s,%s,%s)", (fila[0], title, body, keywords, fila[4]))  
            cont +=1
            print(cont)
        except:
            continue
    cur.execute("commit;")  
