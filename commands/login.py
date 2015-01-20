# coding: utf8
from diesel.protocols.redis import RedisClient

def process(command):
    user_name = command["user_name"]
    password = command["password"]
    print user_name
    print password
    client = RedisClient(host='localhost', port=6391)
    client.select(1)
    pw = client.hget('user_name', user_name)
    if pw == password:
	    return reply(True, 10001, 1, command)
    else:
        print "password is not right : %r" % user_name
    return reply(False, 0, 0, command)

def reply(result, user_id, privilege, command):
    return{'command': command['command'], 'command_index': command['command_index'], \
            "result":result, "user_id":user_id, "privilege":privilege}

def test_proces():
	#TODO
	command = ""
	process(command)