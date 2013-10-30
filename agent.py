from docker import Client
import socket
import redis
import json
import time
import os
import urlparse

url = urlparse.urlparse(os.environ.get('REDIS_URL', 'redis://localhost:6379/'))
pool = redis.ConnectionPool(host=url.hostname, port=url.port, db=0, password=url.password)
redis_connection = redis.StrictRedis(connection_pool=pool)

d = Client()
while True:
    containers = d.containers()
    apps = []
    for container in containers:
        app_name = container['Image']
        if 'app/' in app_name and ':latest' in app_name:
            apps.append([app_name.replace("app/", "").replace(":latest",""), container['Ports'].split("->")[0]])
    redis_connection.publish("app_announce", json.dumps({ socket.gethostname(): apps}))
    time.sleep(10)
