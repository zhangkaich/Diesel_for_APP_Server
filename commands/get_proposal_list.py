# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from proposal_title import ProposalTitle
import data_table

def process(command):
    is_end = True
    start = command['start']
    count = command['count']
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.PROPOSAL_TABLE)
    #sort list by proposal*->time get proposal*->content
    result = client.sort(key="list", pattern="proposal*->time", limit=[start, start+count+1],
    	        get=None, order='ASC', alpha=False, store=None)
    print result
    proposal_title_list = []
    if len(result) > count:
       is_end = False
    actual_count = 0
    for i in result:
        key = "proposal" + i
        print key
        value = client.hgetall(key)
        print value
    	proposal_title_list.append(ProposalTitle(value['title'], value['state'], i, value['content']).data_dict)
        actual_count += 1
        if actual_count == count:
           break
    print proposal_title_list
    return reply(True, command, proposal_title_list, is_end)

def reply(result, command, proposal_title_list, is_end):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'proposal_title_list': proposal_title_list, 'is_end': is_end}
    print result
    return result
