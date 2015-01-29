# coding: utf8

class ProposalTitle(object):

    def __init__(self, title, state, id):
        self._title = title
        self._state = state
        self._id = id

    def __str__(self):
        return '_title [%r], _state[%r], _id[%r]' % (self._title, self._state, self._id)

    def dump_json(self):
        dump_dict = {}
        dump_dict['title'] = self._title
        dump_dict['state'] = self._state
        dump_dict['id'] = self._id
        return dump_dict