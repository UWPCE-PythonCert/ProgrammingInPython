
## FIXME: not ported to py3 yet!

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import random
import threading
import time


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # t = random.random() / 1000
        t = 1.0
        # time.sleep(t)
        self.send_response(200)
        self.end_headers()
        message = str(t) + " " + threading.currentThread().getName()
        self.wfile.write(message)
        self.wfile.write('\n')
        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    # maybe someday?
    pass


if __name__ == '__main__':
    server = ThreadedHTTPServer(('localhost', 37337), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
