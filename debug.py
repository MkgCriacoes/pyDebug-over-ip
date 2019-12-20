import builtins
import requests

__print = print

def print(msg):
    __print(str(msg))
    
    host = "localhost:8080"

    requests.get("http://" + host + "/sendlog?msg=" + str(msg))

builtins.print = print

import main