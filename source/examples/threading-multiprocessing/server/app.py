from itertools import count
import time

i = count()


def app(environ, start_response):
    data = "Hello, World. %d\n" % next(i)
    start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Length", str(len(data)))
                              ])
    time.sleep(0.5)
    return iter([data.encode('utf-8')])
