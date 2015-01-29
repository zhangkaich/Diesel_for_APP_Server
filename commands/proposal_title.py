# coding: utf8

class ProposalTitle(object):

    def __init__(self, title, state, id):
        self.data_dict = {}
        self.data_dict['title'] = title
        self.data_dict['state'] = state
        self.data_dict['id'] = id

    def __str__(self):
        return '_title [%r], _state[%r], _id[%r]' %\
        (self.data_dict['title'], self.data_dict['state'], self.data_dict['id'])

