from docker import Client
import socket
from netaddr import IPAddress
import redis
import json
import time
import os
import urlparse
import netifaces

url = urlparse.urlparse(os.environ.get('REDIS_URL', 'redis://localhost:6379/'))
pool = redis.ConnectionPool(host=url.hostname, port=url.port, db=0, password=url.password)
redis_connection = redis.StrictRedis(connection_pool=pool)

d = Client()


def get_private_ip_or_hostname():
    for iface in netifaces.interfaces():
        if iface.startswith("eth"):
            for address_dict in netifaces.ifaddresses(iface).values():
                if not ":" in address_dict['addr']:
                    if IPAddress(address_dict['addr']).is_private():
                        return address_dict['addr']
    return socket.gethostname()


while True:
    apps = []
    containers = d.containers()  # Get all current containers from docker
    for container in containers:
        app_name = container['Image']
        if 'app/' in app_name and ':latest' in app_name:
            apps.append([app_name.replace("app/", "").replace(":latest",""), container['Ports'].split("->")[0]])
    redis_connection.publish("app_announce", json.dumps({get_private_ip_or_hostname(): apps}))
    time.sleep(10)
