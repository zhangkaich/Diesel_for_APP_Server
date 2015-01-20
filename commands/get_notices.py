# coding: utf8
from diesel.protocols.redis import RedisClient

def process(command):
    client = RedisClient(host='localhost', port=6391)
    client.select(3)
    #get notices
    notices = client.smembers('notices')
    print notices
    return reply(True, notices, command)

def reply(result, notices, command):
    return {'command': command['command'], 'command_index': command['command_index'], \
            "result": result, 'notices': notices}