# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from reconsider_title import ReconsiderTitle
import data_table

def process(command):
    proposal_id = command['proposal_id']
    print "proposal_id %r" %proposal_id
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.PROPOSAL_TABLE)
    proposal_key = "proposal" + str(proposal_id)
    print proposal_key
    value = client.hgetall(proposal_key)
    print value 
    client.select(data_table.RECONSIDER_TABLE)
    key = "reconsider" + str(proposal_id)
    client.hset(key, 'title', value['title'])
    client.hset(key, 'state', value['state'])
    client.hset(key, 'content', value['content'])
    client.hset(key, 'type', 1)
    client.hset(key, 'time', value['time'])
    reconsiderTitle = ReconsiderTitle(value['title'], value['state'], proposal_id, value['content'], 0, 0)
    client.lpush("list", proposal_id)
    #create reconsider

    #delete proposal
    client.select(data_table.PROPOSAL_TABLE)
    client.delete(proposal_key)
    client.lrem("list", proposal_id, 1)
    return reply(True, command, reconsiderTitle)

def reply(result, command, reconsiderTitle):

    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'reconsider_title': reconsiderTitle.data_dict}

    return result
