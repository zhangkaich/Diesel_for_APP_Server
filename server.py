# coding: utf8

import json
import diesel
import struct
from diesel.protocols.redis import RedisClient
from command import Command
from config import Configuration

config=Configuration()
config.get_configuration()
print config.config

def holla_back(addr):
    while True:
        #message = diesel.receive()
        #print '%x\n' % message
        #print '%r\n' % message
        buffer = diesel.receive(4)
        print "%r\n" % buffer
        query_size, = struct.unpack('<i', buffer)
        print "query size %r" % query_size
        message = diesel.receive(query_size)
        print "receive :%r" % message
        command = Command(config.config['command'])
        result = command.handle(message)
        print "reply : %r" % result
        result_size = len(result)
        total_size = result_size
        fmt = "<i%ds" % result_size
        print result_size
        diesel.send(struct.pack(fmt, total_size, result))        

diesel.quickstart(diesel.Service(holla_back, port=config.config['server']['port'], track=True))
