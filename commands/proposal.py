# coding: utf8

class Proposal(object):
    def __init__(self, title, content, type_value, state, time):
        self._title = title
        self._content = content
        self._type = type_value
        self._state = state
        self._time = time

    def __str__(self):
    	return '_title [%r], _content[%r], _type[%r], _state[%r], _time[%r]'\
    	        %(self._title, self._content, self._type, self._state, self._time)