
import threading
import time
import random





def func(n):
    for i in range(n):
        print("hello from thread %s" % threading.current_thread().name)
        time.sleep(random.random() * 2)


threads = []
for i in range(3):
    thread = threading.Thread(target=func, args=(i + 4,))
    thread.start()
    threads.append(thread)







for thread in threads:
    print("joining thread:", thread.name)
    thread.join()
print("all threads finished")

