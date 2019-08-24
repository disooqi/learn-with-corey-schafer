# https://technobeans.com/2012/08/19/tornado-web-sockets/
import tornado.ioloop
import tornado.web
import tornado.websocket

class Socket(tornado.websocket.WebSocketHandler):
    def open(self):
        print "Socket opened"

    def on_message(self, message):
        self.write_message("Msg is " + message)

    def on_close(self):
        print "Socket closed"

class Main(tornado.web.RequestHandler):
        def get(self):
                print "It Works!"

application = tornado.web.Application([
        (r"/", Main),
        (r"/socket", Socket),
        ],debug=True)

