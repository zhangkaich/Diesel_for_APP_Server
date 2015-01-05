
import ujson as json

def handle(command):
    command_dict = json.loads(command)

    if "command" in command_dict:
    	#TODO auto import command file call the process function
    	import login
    	reply = login.process(command_dict)
    	return json.dumps(reply)
    else:
    	 print "Unsupport command"
    	 return {"result":False}
    return {"result":False}

def test_login():
	test_data = {"command": "login", "user_name": "blzhang", "password": "123"}
	json_result = json.dumps(test_data)
	result = handle(json_result)
	print result

def test():
	test_login()