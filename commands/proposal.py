# coding: utf8

class Proposal(object):

    def __init__(self, title, content, type_value, state, time):
        self.data_dict = {}
        self.data_dict['title'] = title
        self.data_dict['content'] = content
        self.data_dict['type'] = type_value
        self.data_dict['state'] = state
        self.data_dict['time'] = time

    def __str__(self):
    	return 'title [%r], content[%r], type[%r], state[%r], time[%r]'\
    	        %(self.data_dict['title'], self.data_dict['content'], self.data_dict['type'],\
    	        	self.data_dict['state'], self.data_dict['time'])