import channel
import subprocess

p = subprocess.Popen(['python', 'child.py'],
                     stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE)
ch = channel.Channel(p.stdin, p.stdout)

ch.send(b"Hello World")
ch.send(42)
ch.send([1,2,3,4])
ch.send({'host':'python.org', 'port':80})
