import diesel
import msgpack
import struct
import json
import simplejson

class TestClient(diesel.Client):
    @diesel.call
    def holla(self, key):
        print "mesage %r" % key
        #print "json dump %r" % simplejson.loads(message) 
        message = {}
        message[1] = {"command": "login", "sequence_id": 1, "user_name": "zhou", "password": "123"}
        message[2] = {"command": "publish_proposal",  "sequence_id": 1, "title": "test", "content": "test"}
        message[3] = {"command": "get_proposal_list",  "sequence_id": 1, "start":0, "count":10}

        message[4] = {"command": "add_comment",  "sequence_id": 7, "proposal_id": 17, "user_name":"name", "comment":"comment comment"}
        message[5] = {"command": "get_comments",  "sequence_id": 7, "proposal_id": 17}
        message[6] = {"command": "del_comment",  "sequence_id": 7, "proposal_id": 17, "comment_index": 1}

        message[7] = {"command": "publish_notice",  "sequence_id": 1, "content": "test1234"}
        message[8] = {"command": "get_notices",  "sequence_id": 1}

        message[9] = {"command": "publish_reconsider",  "sequence_id": 1, "proposal_id":25}
        message[10] = {"command": "get_reconsider_list", "sequence_id": 1, "start":0, "count":10}       
        message[11] = {"user_name": 'zhou', 'sequence_id': 14, 'reconsider_id': 25, 'command': 'judge_reconsider', 'judge_result': False}
        message[12] = {"user_name": 'blzhang', 'sequence_id': 14, 'reconsider_id': 25, 'command': 'judge_reconsider', 'judge_result': True}

        message[13] = {"command": "get_meeting_list", "sequence_id": 1, "start":0, "count":10}
        message[14] = {"command": "add_meeting_comment", "sequence_id": 1, "meeting_id": 9, "user_name":"name", "comment":"comment comment"}
        message[15] = {"command": "get_meeting_people", "sequence_id": 1, "meeting_id": 9}
 
        request = msgpack.dumps(message[int(key)])
        length = len(request)
        fmt = "<i%ds" % length
        
        diesel.send(struct.pack(fmt, length, request))
        buffer = diesel.receive(4)
        print "%r\n" % buffer
        query_size, = struct.unpack('<i', buffer)
        reply = diesel.receive(query_size)
        result = msgpack.loads(reply)
        return result

if __name__ == '__main__':
    def demo():
        client = TestClient('localhost', 4321)
        with client:
            while True:
                msg = raw_input('message> ')
                print "reply> %s" % client.holla(msg)

    diesel.quickstart(demo)
