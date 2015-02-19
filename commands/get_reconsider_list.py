# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from reconsider_title import ReconsiderTitle

def process(command):
    start = command['start']
    count = command['count']
    client = RedisClient(host='localhost', port=6391)
    client.select(4)
    #sort list by proposal*->time get proposal*->content
    result = client.sort(key="list", pattern="reconsider*->time", limit=[start, start+count],
    	        get=None, order='ASC', alpha=False, store=None)
    print result
    reconsider_title_list = []
    for i in result:
        key = "reconsider" + i
        value = client.hgetall(key)
    	reconsider_title_list.append(ReconsiderTitle(value['title'], value['state'], i, value['content'], value['agree_count'], value['disagree']).data_dict)
    print reconsider_title_list
    return reply(True, command, reconsider_title_list)

def reply(result, command, reconsider_title_list):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'reconsider_title_list': reconsider_title_list}
    print [result]
    return result
