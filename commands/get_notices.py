# coding: utf8
from diesel.protocols.redis import RedisClient
import data_table

def process(command):
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.NOTICE_TABLE)
    #get notices
    notices = client.smembers('notices')
    print type(notices)
    print notices
    return reply(True, list(notices), command)

def reply(result, notices, command):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result": result, 'notices': notices}
    return result
