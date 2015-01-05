import diesel

class TestClient(diesel.Client):
    @diesel.call
    def holla(self, message):
        diesel.send(message + '\r\n')
        reply = diesel.receive()
        return reply.strip()

if __name__ == '__main__':
    def demo():
        client = TestClient('localhost', 4321)
        with client:
            while True:
                msg = raw_input('message> ')
                print "reply> %s" % client.holla(msg)

    diesel.quickstart(demo)