# coding: utf8

class Comment(object):

    def __init__(self, user_name, comment, time):
        self.data_dict = {}
        self.data_dict['user_name'] = user_name
        self.data_dict['comment'] = comment
        self.data_dict['time'] = time

    def __str__(self):
        return 'user_name[%r], comment[%r], time[%r]' %\
        (self.data_dict['user_name'], self.data_dict['comment'], self.data_dict['time'])