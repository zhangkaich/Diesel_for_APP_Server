# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from reconsider_title import ReconsiderTitle
import data_table

def process(command):
    start = command['start']
    count = command['count']
    is_end = True
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.RECONSIDER_TABLE)
    #sort list by proposal*->time get proposal*->content
    result = client.sort(key="list", pattern="reconsider*->time", limit=[start, start+count+1],
    	        get=None, order='ASC', alpha=False, store=None)
    print result
    reconsider_title_list = []
    if len(result) > count:
       is_end = False
    actual_count = 0
    for i in result:
        key = "reconsider" + i
        value = client.hgetall(key)
        agree_key = "agree_reconsider" + str(i)
        disagree_key = "disagree_reconsider" + str(i)
        agree_count = client.scard(agree_key)
        disagree_count = client.scard(disagree_key)
    	reconsider_title_list.append(ReconsiderTitle(value['title'], value['state'], i, value['content'], agree_count, disagree_count).data_dict)
        actual_count += 1
        if actual_count == count:
           break
    print reconsider_title_list
    return reply(True, command, reconsider_title_list, is_end)

def reply(result, command, reconsider_title_list, is_end):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'reconsider_title_list': reconsider_title_list, 'is_end': is_end}
    print result
    return result
