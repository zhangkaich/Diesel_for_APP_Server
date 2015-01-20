from diesel.protocols.redis import RedisClient

def process(command):
    #get account id
    client = RedisClient('localhost', 6391)
    client.select(1)
    accout_id_key = "accout_id"
    accout_id_lock = "accout_id_lock"
    try:
        with RedisLock(client, accout_id_lock, timeout=lock_timeout) as lock:
            accout_id = client.get(accout_id_key)
            client.set(accout_id_key, int(accout_id) + 1)
    except LockNotAcquired:
        pass
    #create account: name password privilege

    return {"result":False, "user_id":0, "privilege":0}

def test_proces():
	#TODO
	command = ""
	process(command)