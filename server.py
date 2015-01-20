# coding: utf8

import json
import diesel

from diesel.protocols.redis import RedisClient
from command import Command
from config import Configuration

config=Configuration()
config.get_configuration()
print config.config

def holla_back(addr):
    while True:
        message = diesel.until_eol()
        command = Command(config.config['command'])
        result = command.handle(message)
        print "reply : %r" % result
        diesel.send(result)

diesel.quickstart(diesel.Service(holla_back, port=config.config['server']['port'], track=True))