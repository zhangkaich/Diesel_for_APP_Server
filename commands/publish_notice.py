# coding: utf8
from diesel.protocols.redis import RedisClient
import data_table

def process(command):
    notice = command["content"]
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.NOTICE_TABLE)
    #Write notice to redis
    #Set
    print notice.encode('UTF8')
    result = client.sadd('notices', notice.encode('UTF8'))
    print "sadd result", result
    if result:
        return reply(True, command)
    else:
        return reply(False, command)

def reply(result, command):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result": result,}
    return result
