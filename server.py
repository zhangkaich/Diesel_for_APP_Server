# tcp_holla_server.py
import json
from diesel.protocols.redis import RedisClient
import diesel
import command

def holla_back(addr):
    while True:
        message = diesel.until_eol()
        result = command.handle(message)
        print "reply : %r" % result
        diesel.send(result)

diesel.quickstart(diesel.Service(holla_back, 4321))