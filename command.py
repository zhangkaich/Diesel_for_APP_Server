# coding: utf8
import ujson as json
import msgpack
import commands.login as login
import commands.get_notices as get_notices
import commands.publish_notice as publish_notice
import commands.get_proposal as get_proposal
import commands.publish_proposal as publish_proposal
import commands.get_proposal_list as get_proposal_list
import commands.add_comment as add_comment
import commands.del_comment as del_comment
import commands.get_comments as get_comments
import commands.get_reconsider_list as get_reconsider_list
import commands.publish_reconsider as publish_reconsider


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
        handle_dict = {}
        handle_dict['login'] = login
        handle_dict['publish_notice'] = publish_notice
        handle_dict['get_notices'] = get_notices
        handle_dict['publish_proposal'] = publish_proposal
        handle_dict['get_proposal_list'] = get_proposal_list
        handle_dict['add_comment'] = add_comment
        handle_dict['del_comment'] = del_comment
        handle_dict['get_comments'] = get_comments
        handle_dict['get_proposal'] = get_proposal
        handle_dict['get_reconsider_list'] = get_reconsider_list
        handle_dict['publish_reconsider'] = publish_reconsider

        try:
            command_dict = msgpack.loads(command)
            print "command_dict %r" % command_dict
            if "command" in command_dict:
            	#TODO auto import command file call the process function
                print "command"
                if command_dict['command'] in handle_dict:
                    ##print command_dict['command']
                    reply = handle_dict[command_dict['command']].process(command_dict)
                else:
                    print command_dict['command']

            	return msgpack.dumps(reply)
            else:
            	 print "Unsupport command"
            	 return msgpack.dumps({"result":False})
            return msgpack.dumps({"result":False})
        except Exception,e:
            print e
            return msgpack.dumps({"result":False})

def test_login():
	test_data = {"command": "login", "user_name": "blzhang", "password": "123"}
	json_result = json.dumps(test_data)
	result = handle(json_result)
	print result

def test():
	test_login()
