from re import search
import grpc
from concurrent import futures
import serv_pb2_grpc
import serv_pb2
import psycopg2
import connect
import time as t

class Search(serv_pb2_grpc.Search):
    def __init__(self, *args, **kwargs):
        pass
    def getResponce(self, request, context):
        q= f"SELECT * FROM Items;"
        item = []
        response=[]
        message = request.message
        result = f"{message}"
        cur.execute(q)
        qres= cur.fetchall()
        for i in qres:
            if item in i[1]:
                item.append(i)
        for i in item:
            result = dict()
            result['url'] = i[1]
            result['title'] = i[2]
            result['description'] = i[3]
            result['sn'] = i[4]
            response.append(result)

        print(serv_pb2.SearchResults(search=response))
        return(serv_pb2.SearchResults(search=response))


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    serv_pb2_grpc.add_SearchServicer_to_server(serv_pb2_grpc.Search,server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__== "__main__":
    t.sleep(10)
    con = connect.conexion()
    cur = con.cursor()
    serv()
    print("conected")