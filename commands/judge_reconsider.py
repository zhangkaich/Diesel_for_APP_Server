# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from reconsider_title import ReconsiderTitle
import data_table

def check_user_in_judge_set(client, user_name, reconsider_id, judge_result):
    #SISMEMBER check the member is exist
    agree_key = "agree_reconsider" + str(reconsider_id)
    agree_result = client.sismember(agree_key, user_name)
    disagree_key = "disagree_reconsider" + str(reconsider_id)
    disagree_result = client.sismember(disagree_key, user_name)
    if judge_result:
       if not agree_result:
          #add
          client.sadd(agree_key, user_name) 
       if disagree_result:
          #remove
          client.srem(disagree_key, user_name)
    else:
       if not disagree_result:
          #add
          client.sadd(disagree_key, user_name)
       if agree_result:
          #remove
          client.srem(agree_key, user_name)
    agree_count = client.scard(agree_key)
    disagree_count = client.scard(disagree_key)
    return agree_count, disagree_count


def process(command):
    reconsider_id = command['reconsider_id']
    judge_result = command['judge_result']
    user_name = command['user_name']
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.RECONSIDER_TABLE)
    #sort list by proposal*->time get proposal*->content
    #
    key = "reconsider" + str(reconsider_id)
    if client.exists(key):
       agree_count, disagree_count = check_user_in_judge_set(client, 
                                     user_name, reconsider_id, judge_result)
       value = client.hgetall(key)
       reconsiderTitle = ReconsiderTitle(value['title'], value['state'], reconsider_id, value['content'], agree_count, disagree_count)
       return reply(True, command, reconsiderTitle)
    else:
       return {'command': command['command'], 'sequence_id': command['sequence_id'], \
               "result": False}

def reply(result, command, reconsider):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'reconsider_title_list': reconsider.data_dict}
    print result
    return result
