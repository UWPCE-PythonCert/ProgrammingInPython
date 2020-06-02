import channel
import sys

ch = channel.Channel(sys.stdout, sys.stdin)
while True:
    item = ch.recv()
    ch.send(("child", item))
