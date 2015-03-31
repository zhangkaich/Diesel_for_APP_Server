# coding: utf8
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
import data_table

lock_timeout = 3

def process(command):
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.PROPOSAL_TABLE)
    proposal_id_lock = "proposal_id_lock"
    proposal_id_key = "uuid"
    proposal_id = 0
    #get proposal id
    try:
        with RedisLock(client, proposal_id_lock, timeout=lock_timeout) as lock:
            proposal_id = client.get(proposal_id_key)
            client.set(proposal_id_key, int(proposal_id) + 1)
    except LockNotAcquired:
        return reply(False, command)
    proposeal_key = "proposal" + str(proposal_id)
    if command['title'] is None or len(command['title']) == 0:
       client.hset(proposeal_key, 'title', " ")
    else:
       client.hset(proposeal_key, 'title', command['title'])
    if command['content'] is None or len(command['content']) == 0:
       client.hset(proposeal_key, 'content', " ")
    else:
       client.hset(proposeal_key, 'content', command['content'])
    #提议: 复议/未复议
    #复议: 赞同/反对
    #会议: 进行中/已完成/为开始
    #决议: 执行
    client.hset(proposeal_key, 'state', 0)
    client.hset(proposeal_key, 'type', 0)
    client.hset(proposeal_key, 'time', time.time())
    client.lpush("list", proposal_id)
    #set proposal title
    #proposal_id: title: ***
    #             content: ***
    #             state: ***
    #             time:
    #SORT list get proposal_*->time
    #sort list by proposal*->time get proposal*->content
    return reply(True, command, proposal_id)

def reply(result, command, proposal_id):

    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, "id":int(proposal_id)}

    return result
