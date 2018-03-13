# https://os.mbed.com/cookbook/Websockets-Server
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket


class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection (Socket opened)'

    def on_message(self, message):
        print 'message received:  %s' % message
        # Reverse Message and send it back
        print 'sending back message: %s' % message[::-1]
        self.write_message(message[::-1])

    def on_close(self):
        print 'connection closed (Socket closed)'

    def check_origin(self, origin):
        return True


class Main(tornado.web.RequestHandler):
    '''
    https://technobeans.com/2012/08/19/tornado-web-sockets/
    '''
    def get(self):
        print "It Works!"


application = tornado.web.Application([
    (r"/", Main),
    (r'/ws', WSHandler),
], debug=True)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    myIP = socket.gethostbyname(socket.gethostname())
    print '*** Websocket Server Started at %s***' % myIP
    tornado.ioloop.IOLoop.instance().start()