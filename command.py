# coding: utf8
import ujson as json
import commands.login as login
import commands.get_notices as get_notices
import commands.publish_notice as publish_notice
import commands.get_notices as get_notices

class Command(object):
    def __init__(self, command_list):
        self.command_handles = []
        #try:
        #    for command in command_list:
        #        self.command_handles.append(
        #            getattr(__import__()))
        #except (KeyError, ImportError), exception_data:
        #    print "exception %r", (exception_data)


    #TODO append function to dict then run the command
    def handle(self, command):
        try:
            command_dict = json.loads(command)

            if "command" in command_dict:
            	#TODO auto import command file call the process function
                if cmp(command_dict['command'], 'login') == 0:
                    print 'login'
                    reply = login.process(command_dict)
                elif cmp(command_dict['command'], 'publish_notice') == 0:
                    print 'publish_notice'
                    reply = publish_notice.process(command_dict)
                elif cmp(command_dict['command'], 'get_notices') == 0:
                    print 'get_notices'
                    reply = get_notices.process(command_dict)
                else:
                    print command_dict['command']

            	return json.dumps(reply)
            else:
            	 print "Unsupport command"
            	 return json.dumps({"result":False})
            return json.dumps({"result":False})
        except Exception,e:
            print e
            return json.dumps({"result":False})

def test_login():
	test_data = {"command": "login", "user_name": "blzhang", "password": "123"}
	json_result = json.dumps(test_data)
	result = handle(json_result)
	print result

def test():
	test_login()