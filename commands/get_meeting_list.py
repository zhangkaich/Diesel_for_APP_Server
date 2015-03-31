# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from meeting_title import MeetingTitle
import data_table

def process(command):
    start = command['start']
    count = command['count']
    is_end = True
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.MEETING_TABLE)
    #sort list by proposal*->time get proposal*->content
    result = client.sort(key="list", pattern="meeting*->time", limit=[start, start+count+1],
    	        get=None, order='ASC', alpha=False, store=None)
    print result
    meeting_title_list = []
    if len(result) > count:
       is_end = False
    actual_count = 0
    for i in result:
        key = "meeting" + i
        value = client.hgetall(key)
        agree_key = "agree_meeting" + str(i)
        disagree_key = "disagree_meeting" + str(i)
        agree_count = client.scard(agree_key)
        disagree_count = client.scard(disagree_key)
    	meeting_title_list.append(MeetingTitle(value['title'], value['state'], i, value['content'], agree_count, disagree_count).data_dict)
        actual_count += 1
        if actual_count == count:
           break
    print meeting_title_list
    return reply(True, command, meeting_title_list, is_end)

def reply(result, command, meeting_title_list, is_end):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, 'meeting_list': meeting_title_list, 'is_end': is_end}
    print result
    return result
