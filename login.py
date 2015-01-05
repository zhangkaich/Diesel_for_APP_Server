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
	    return {"result":True, "user_id":10001, "privilege":1}
    else:
        print "password is not right : %r" % user_name
    return {"result":False, "user_id":0, "privilege":0}

def test_proces():
	#TODO
	command = ""
	process(command)