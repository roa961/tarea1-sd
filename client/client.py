from flask import Flask

import redis
import grpc

r_main = redis.Redis(host="172.20.1.3", port=6379, db=0) # Principal
r_replica1 = redis.Redis(host="172.20.1.4", port=6379, db=0) # Replica Nº1
r_replica2 = redis.Redis(host="172.20.1.5", port=6379, db=0) # Replica Nº2

try:
    print(r_main.ping())
    print(r_replica1.ping())
    print(r_replica2.ping())
except:
    print("error")
