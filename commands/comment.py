# coding: utf8

class Comment(object):

    def __init__(self, user_id, user_name, comment, time):
        self.user_id = user_id
        self.user_name = user_name
        self.comment = comment
        self.time = time

    def __str__(self):
        return 'user_id [%r], user_name[%r], comment[%r]' % (self.user_id, self.user_name, self.comment)

    def dump_json(self):
        dump_dict = {}
        dump_dict['title'] = self._title
        dump_dict['state'] = self._state
        dump_dict['id'] = self._id
        return dump_dict