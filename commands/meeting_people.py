# coding: utf8

class MeetingPeople(object):

    def __init__(self, id, user_name):
        self.data_dict = {}
        self.data_dict['id'] = int(id)
        self.data_dict['user_name'] = user_name
  
    def __str__(self):
        return '_title [%r], _state[%r], _id[%r]' %\
        (self.data_dict['title'], self.data_dict['state'], self.data_dict['id'])

