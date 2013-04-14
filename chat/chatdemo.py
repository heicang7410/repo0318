import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.websocket

import uuid


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class ChatSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()

    def open(self):
        print "Welcome chat room"
        ChatSocketHandler.waiters.add(self)

    def on_close(self):
        print "Quit chat room"
        ChatSocketHandler.waiters.remove(self)

    def on_message(self, message):
        message = tornado.escape.json_decode(message)
        chat = {
            "id": str(uuid.uuid4()),
            "body": message['body']
        }
        for waiter in ChatSocketHandler.waiters:
            waiter.write_message(chat)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/chatsocket", ChatSocketHandler),
])

if __name__ == "__main__":
    application.listen(9097)
    tornado.ioloop.IOLoop.instance().start()
