# coding: utf8
from diesel.protocols.redis import RedisClient
import data_table

def process(command):
    user_name = command["user_name"]
    password = command["password"]
    print user_name
    print password
    client = RedisClient(host='localhost', port=6391)
    client.select(data_table.USER_TABLE)
    pw = client.hget('user_name', user_name)
    if pw == password:
        user_id = client.hget('user_id', user_name)
        return reply(True, int(user_id), 1, command)
    else:
        print "password is not right : %r" % user_name
    return reply(False, 0, 0, command)

def reply(result, user_id, privilege, command):
    result = {'command': command['command'], 'sequence_id': command['sequence_id'], \
            "result":result, "user_id":user_id, "privilege":privilege}
    result["proposal_list"]=[{'id': 234, 'title': 'test0'}, {'id': 235, 'title': 'test1'} ]
    print "login"
    print [result]
    return result

def test_proces():
	#TODO
	command = ""
	process(command)
