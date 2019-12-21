import builtins
import requests
import threading

__print = print

class threadEnviar(threading.Thread):
    msg = None
    host = None

    def __init__(self, host, msg):
        threading.Thread.__init__(self)
        self.host = host
        self.msg = msg

    def run(self):
        requests.get("http://" + self.host + "/sendlog?msg=" + str(self.msg))

def print(msg):
    __print(str(msg))
    
    host = "localhost:8080"

    threadEnviar(host, msg).start()

builtins.print = print

import main