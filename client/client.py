from flask import Flask, request, render_template, app

import proto_web_pb2 as pb2_grpc
import proto_web_pb2_grpc as pb2
import redis
import grpc

r_main = redis.Redis(host="172.20.1.3", port=6379, db=0) # Principal
r_replica1 = redis.Redis(host="172.20.1.4", port=6379, db=0) # Replica Nº1
r_replica2 = redis.Redis(host="172.20.1.5", port=6379, db=0) # Replica Nº2

class Cliente(object):
    def __init__(self):
        self.host = 'server'
        self.port = 50051
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = pb2.SearchStub(self.channel)
    def get_url(self, message):
        message = pb2_grpc.Message(message = message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)

@app.route('/search', methods = ['GET'])

def busqueda(self):
    cliente = Cliente()
    search = request.args['search']
    search = "hola" 
    if r_main.get(search) == None:
        web = cliente.get_url(message=search)
        r_main.set(search,str(web))
    elif r_main.get(search):
        print(r_main.get(search))
        
