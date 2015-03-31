# coding: utf8
import ujson as json
import time
from diesel.protocols.redis import RedisClient, RedisTransactionError, RedisLock, LockNotAcquired
from comment import Comment
import data_table

def process(command):
    meeting_id = command['meeting_id']
    comment = command['comment']
    user_name = command['user_name']

    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.MEETING_TABLE)
    #check propsoal 
    key = "meeting" + str(meeting_id)
    print "key %r" % key
    result = client.exists(key)
    if not result:
       return {'command': command['command'], 'sequence_id': command['sequence_id'], "result": result}

    #sadd
    comment_id = "comment_" + str(meeting_id)
    client.lpush(comment_id, user_name+'^'+comment+'^'+str(time.time()))

    comments = []
    comment_list = client.lrange(comment_id, 0, -1)
    for comment in comment_list:
        result = comment.split('^')
        if len(result)>=3:
            comments.append(Comment(result[0], result[1], result[2]).data_dict)
    return reply(True, command, comments)

def reply(result, command, comments):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, "comments":comments}
    return result
