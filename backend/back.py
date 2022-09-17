from re import search
import grpc
from concurrent import futures
import proto_web_pb2 as pwb2
import proto_web_pb2_grpc as pwb2gc
from time import sleep
import psycopg2 as ps


class SearchService(pwb2gc.SearchServicer):
    def __init__(self, *args, **kwargs):
        pass
    def GetServerResponse(self, request, context):
        item = []
        response=[]
        message = request.message
        result = f'"{message}"'
        cur.execute("SELECT * FROM WEBS;")
        qres = cur.fetchall()
        for i in qres:
            if message in i[1]:
                item.append(i)
        if len(item) == 0:
            result = dict()
            ##result['id'] = 0
            result['title'] = "No hay datos"
            result['description'] = "No hay datos"
            #result['keywords'] = "No hay datos"
            result['url'] = "No hay datos"
            response.append(result)
            return pwb2.SearchResults(web=response)
        for j in item:
            result = dict()
            ##result['id'] = j[0]
            result['title'] = j[1]
            result['description'] = j[2]
            #result['keywords'] = j[3]
            result['url'] = j[4]
            print(result)
            response.append(result)

        print(pwb2.SearchResults(web=response))

        return pwb2.SearchResults(web=response)


def serv():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    pwb2gc.add_SearchServicer_to_server(SearchService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    

if __name__== "__main__":
    sleep(15)
    try:
        con = ps.connect("dbname=paginas user=postgres password=postgres host=postgresql")
        print("Servidor conectado a la db")
    except:
        print("No fue posible conectarse a la db")
    cur =con.cursor()
    serv()
    