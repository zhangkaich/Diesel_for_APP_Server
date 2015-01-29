# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from proposal_title import ProposalTitle

def process(command):
    proposal_id = command['proposal_id']
    comment = command['comment']
    user_id = command['user_id']
    client = RedisClient(host='localhost', port=6391)
    client.select(2)
    #sadd
    comment_id = "comment_" + str(proposal_id)
    client.sadd(comment_id, user_id+'^'+comment)

    comment_list = clinet.smembers(comment_id)
    for comment in comment_list:

    return reply(True, command, proposal_title_list)

def reply(result, command, proposal_title_list):
    return{'command': command['command'], 'command_index': command['command_index'], \
            "result":result, 'proposal_title_list': proposal_title_list}
