from re import search
import grpc
from concurrent import futures
import proto_web_pb2
import proto_web_pb2_grpc
import connect
from time import sleep
import psycopg2 as ps


class Search(proto_web_pb2_grpc.SearchServicer):
    def __init__(self, *args, **kwargs):
        pass
    def GetServerResponse(self, request, context):
        query= "SELECT * FROM WEBS;"
        item = []
        response=[]
        message = request.message
        result = f'"{message}"'
        cur.execute(query)
        qres = cur.fetchall()
        for i in qres:
            if message in i[1]:
                item.append(i)
        for j in item:
            result = dict()
            result['id'] = j[1]
            result['title'] = j[2]
            result['description'] = j[3]
            result['url'] = j[4]
            #
            response.append(result)

        print(proto_web_pb2.Search(search=response))
        return proto_web_pb2.Search(search=response)


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    proto_web_pb2_grpc.add_SearchServicer_to_server(Search(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
def connectdb():
    con = ps.connect("dbname=paginas user=postgres password=postgres host=postgresql")
    return con
if __name__== "__main__":
    sleep(15)
    try:
        con = ps.connect("dbname=paginas user=postgres password=postgres host=postgresql")
        print(con)
        cur =con.cursor()
        print("conectado")
        #serv()
    except:
        print("no se pudo conectar")
    