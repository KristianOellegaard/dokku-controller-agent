from docker import Client
import socket
import redis
import json
import time

redis_connection = redis.StrictRedis()

d = Client()
while True:
    containers = d.containers()
    apps = []
    for container in containers:
        apps.append([container['Image'].replace("app/", "").replace(":latest",""), container['Ports'].split("->")[0]])
    redis_connection.publish("app_announce", json.dumps({ socket.gethostname(): apps}))
    time.sleep(40)
