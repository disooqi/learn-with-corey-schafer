# https://ws4py.readthedocs.io/en/latest/sources/clienttutorial/
# https://askubuntu.com/questions/142871/how-to-run-asynchronous-tasks-in-python-gobject-introspection-apps
from ws4py.client.threadedclient import WebSocketClient


class DummyClient(WebSocketClient):
    def opened(self):
        print 'DummyClient ... connected'
        # def data_provider():
        #     for i in 'disooqi':
        #         yield i
        #
        # self.send(data_provider())
        # name = "Mohamed Eldesouki"
        # for i in range(len(name)):
        #     print name[:i+1], '(from print)'
        #     self.send(name[:i+1])
        # else:
        #     self.send("Mariam")


    def closed(self, code, reason=None):
        print "disooqi Closed down", code, reason

    def received_message(self, m):
        print m
        #if len(m) == 175:
        #self.close(reason='Bye bye')

if __name__ == '__main__':
    try:
        ws = DummyClient('ws://localhost:8888/ws', protocols=['http-only', 'chat'])
        ws.connect()
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()