# coding: utf8

class MeetingTitle(object):

    def __init__(self, title, state, id, content, agree_count, disagree_count):
        self.data_dict = {}
        self.data_dict['title'] = title
        self.data_dict['state'] = int(state)
        self.data_dict['id'] = int(id)
        self.data_dict['context'] = content
        self.data_dict['agree_count'] = int(agree_count)
        self.data_dict['disagree_count'] = int(disagree_count)
  
    def __str__(self):
        return '_title [%r], _state[%r], _id[%r]' %\
        (self.data_dict['title'], self.data_dict['state'], self.data_dict['id'])

