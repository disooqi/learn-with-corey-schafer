from ws4py.client.threadedclient import WebSocketClient

class EchoClient(WebSocketClient):
    def opened(self):
        self.send("Hello Chetan")

    def closed(self, code, reason=""):
        print "Closed down", code, reason

    def received_message(self, m):
        print "Received from server: %s" % (str(m))

if __name__ == '__main__':
    try:
        ws = EchoClient('http://localhost:8888/socket', protocols=['http-only', 'chat'])
        ws.daemon = False
        ws.connect()
    except KeyboardInterrupt:
        ws.close()
    finally:
        ws.close()