import diesel
import msgpack
import struct
import json
import simplejson

class TestClient(diesel.Client):
    @diesel.call
    def holla(self, message):
        print "mesage %r" % message
        #print "json dump %r" % simplejson.loads(message)
        message = {"command": "login", "sequence_id": 1, "user_name": "blzhang", "password": "123"}
        message1 = {"command": "publish_notice",  "sequence_id": 1, "content": "test"}
        message2 = {"command": "get_notices",  "sequence_id": 1}
        message3 = {"command": "get_proposal_list",  "sequence_id": 1, "start":0, "count":10}
        message4 = {"command": "publish_reconsider",  "sequence_id": 1, "proposal_id":7}
        message5 = {"command": "get_reconsider_list", "sequence_id": 1, "start":0, "count":10}
        message6 = {"command": "publish_proposal",  "sequence_id": 1, "title": "test", "content": "test"}
        message7 = {"command": "add_comment",  "sequence_id": 7, "proposal_id": 7, "user_name":"name", "comment":"comment comment"}
        request = msgpack.dumps(message4)
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
