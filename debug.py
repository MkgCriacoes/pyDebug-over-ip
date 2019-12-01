import builtins
#import urllib.request
import requests

__print = print

def print(msg):
    __print(str(msg))
    
    #urllib.request.urlopen("localhost/msg/" + str(msg))
    host = "localhost:8080"

    requests.get("http://" + host + "?msg=" + str(msg))

builtins.print = print

import main