# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from proposal_title import ProposalTitle
import data_table

def process(command):
    proposal_id = command['proposal_id']
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.PROPOSAL_TABLE)
    #get proposal
    #get proposal comment

    return reply(True, command, proposal_title_list)

def reply(result, command, proposal_title_list):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'proposal_list': proposal_title_list}
    return result
