# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from proposal_title import ProposalTitle

def process(command):
    start = command['start']
    count = command['count']
    client = RedisClient(host='localhost', port=6391)
    client.select(2)
    #sort list by proposal*->time get proposal*->content
    result = client.sort(key="list", pattern="proposal*->time", limit=[start, start+count],
    	        get=None, order='ASC', alpha=False, store=None)
    print result
    proposal_title_list = []
    for i in result:
        key = "proposal" + i
        value = client.hgetall(key)
    	proposal_title_list.append(ProposalTitle(value['title'], value['state'], i).dump_json())
    print proposal_title_list
    return reply(True, command, proposal_title_list)

def reply(result, command, proposal_title_list):
    return{'command': command['command'], 'command_index': command['command_index'], \
            "result":result, 'proposal_title_list': proposal_title_list}
