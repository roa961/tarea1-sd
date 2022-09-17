from flask import Flask, request, render_template, app

import proto_web_pb2 as pb2
import proto_web_pb2_grpc as pb2_grpc
import redis
import grpc
import time

r_main = redis.Redis(host="redis-master", port=6379, db=0) # Principal
r_main.flushall()
app = Flask(__name__)

class Cliente(object):
    def __init__(self):
        self.host = "servidor"
        self.port = "50051"
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        message = pb2.Message(message = message)
        print(f'{message}')
        stub = self.stub.GetServerResponse(message)
        return stub

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/search', methods = ['GET'])

def busqueda():
    cliente = Cliente()
    search = request.args['search']
    
    if r_main.get(search) == None:
        web = cliente.get_url(message=search)
        if len(str(web)) == 84:
            return render_template('index.html', busqueda = search ,datos = web, origen = "No hay datos de la búsqueda en Postgres")
        r_main.set(search,str(web))
        return render_template('index.html', datos = web, origen = "Datos provenientes de Postgres")

    elif r_main.get(search) != None:
        data = r_main.get(search).decode("utf-8")
        return render_template('index.html', datos = data, origen = "Datos provenientes de Redis")

if __name__ == "__main__":
    time.sleep(20)
