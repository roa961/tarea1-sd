from re import search
import grpc
from concurrent import futures
import proto_web_pb2
import proto_web_pb2_grpc
import psycopg2
import connect
import time as t


class Search(proto_web_pb2_grpc.SearchServicer):
    def __init__(self, *args, **kwargs):
        pass
    def GetServerResponse(self, request, context):
        query= "SELECT * FROM WEBS;"
        item = []
        response=[]
        message = request.message
        result = f"{message}"
        cur.execute(query)
        qres = cur.fetchall()
        for i in qres:
            if item in i[1]:
                item.append(i)
        for i in item:
            result = dict()
            result['id'] = i[1]
            result['title'] = i[2]
            result['description'] = i[3]
            result['url'] = i[4]
            #
            response.append(result)

        print(proto_web_pb2.Search(search=response))
        return(proto_web_pb2.Search(search=response))


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    proto_web_pb2_grpc.add_SearchServicer_to_server(Search(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__== "__main__":
    t.sleep(20)
    con = connect.conexion()
    print("conectado")
    cur = con.cursor()
    serv()