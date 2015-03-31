# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from meeting_people import MeetingPeople
import data_table

def process(command):
    meeting_id = command['meeting_id']
    
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.RECONSIDER_TABLE)
    
    agree_key = "agree_reconsider" + str(meeting_id)
    disagree_key = "disagree_reconsider" + str(meeting_id)
    agree_members_list = []
    agree_members = list(client.smembers(agree_key))
    client.select(data_table.USER_TABLE)
    for p in agree_members:
       id = client.hget('user_id', p)
       agree_members_list.append(MeetingPeople(id, p).data_dict)
    disagree_members_list = []
    disagree_members = list(client.smembers(disagree_key))
    for p in disagree_members:
       id = client.hget('user_id', p)
       disagree_members_list.append(MeetingPeople(id, p).data_dict)
    
    return reply(True, command, agree_members_list, disagree_members_list)

def reply(result, command, agree_members, disagree_members):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, "agree_members": agree_members, "disagree_members": disagree_members}
    print result
    return result
