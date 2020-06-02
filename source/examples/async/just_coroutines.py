#!/usr/bin/env python3

"""
Just coroutines...

Some experimental code working with coroutines by themselves,
outside of an async framework or event loop.

Hopefully, this will help us better understand how they work.
"""

async def corout():
    print("running corout")
    return "something returned"

# Note that the returned value gets tacked on to the StopIteration

async def corout2():
    print("running corout2")
    await corout()

# # make a coroutine
# # cr = corout2()

# # run it with a send:
# # cr.send(None)

# """
# Now we have a a coroutine with an await in it -- let's make it do a little something:
# """

from types import coroutine

"""applying the coroutine decorator makes a generator a coroutine, and thus an awaitable object.
"""

@coroutine
def do_nothing():
    """
    Here is one that does absolutely nothing
    but it can be awaited.
    """
    yield "something from do_nothing"

# """
# only generator-based coroutines can actually pause execution itself -- an asyc def coroutine can only call await on another "awaitable" so at the bottom of the pile there will be a generator-based coroutine.

# In common use, you will use a framework like asyncio that provides both the event loop and the low level awaitable objects.
# """

# """But we can now we can make another coroutine that awaits on the first one:
# """

async def do_a_few_things(num=3):
    # a loop for multiple things
    for i in range(num):
        print(f"in the loop for the {i}th time")
        res = await do_nothing()
        print("res is:", res)
    return "do a few things result"

# create it:
daft = do_a_few_things(5)

# and run it:
# daft.send(None)

# # That just went into the loop:

# # to keep going, we keep calling send() until we get the StopIteration:
while True:
    try:
        daft.send(None)
    except StopIteration as si:
        print("The awaitable is complete")
        print("passed out:", si)
        break

# """
# This looks a lot like generators, doesn't it?? But there are some differences:

# First, we're passing in None to the ``.send()`` method -- it, in fact,
# requires a value -- but what is that value used for?

# You may recall from generators, that send, naturally, sends a value into the generator here's and example of that:
# """

# def gen():
#     for i in range(3):
#         res = yield i
#         print(f"loop: {i}, result: {res}")
#     return "returned from gen"

# g = gen()

# g.send(None)

# g.send(45)
# g.send(60)
# g.send(60)

# """
# Notice how the StopIteration has the return value as its message.

# So how does this work with coroutines?

# It doesn't -- coroutines do not support sending data in - they pass out results to the main loop, and then finally return something, which gets caught in the StopIteration exception -- but the value sent in is ignored.

# This is because coroutines were originaly built from generators, and they still borrow the same methods -- even though they don't do anythign with the value sent in.

# And if you have nested coroutines, the values do get passed up the chain one at a time.
# """

print("\n\n*********\n\n")

@coroutine
def nothing():
    """
    Here is one that does absolutely nothing
    but it can be awaited.
    """
    yield "from nothing"
    return ("returned from nothing")

@coroutine
def count(num):
    """
    And here is one that does absolutely nothing
    but it can be awaited multiple times, and will return
    a value each time.
    """
    for i in range(num):
        yield f"count: {i}"

async def do_a_few_things(num=3, name="no_name"):
    # a loop for multiple things
    for i in range(num):
        print(f'\nin the "{name}" loop for the {i}th time')
        from_await = await nothing()
        print("value returned from await:", from_await)

# create it:
daft = do_a_few_things(5, "first one")

# and start it off:
daft.send(None)

# # That just went into the loop:

# # to keep going, we keep calling send() until we get the StopIteration:
# i = 0
# while True:
#     i+=1
#     print(f"{i}th time in the outer while loop")
#     try:
#         res = daft.send(i)
#         print("result of send:", res)
#     except StopIteration:
#         print("The awaitable is complete")
#         break






# """
# OK, now we have what we need to make something that might
# look a bit like a task loop
# """

print("\n\n*********\n\n")


@coroutine
def nothing():
    yield "yielded from nothing"
    return ("returned from nothing")


@coroutine
def count(num):
    """
    Here is one that loops a bit and returns a count
    """
    for i in range(num):
        yield f"count: {i}"
    return "returned from count"

# and this one loops a bit more, calling count
async def do_a_few_things(num=3, name="no_name"):
    # a loop for multiple things
    for i in range(num):
        print(f'in the "{name}" loop for the {i}th time')
        from_await = await count(i + 2)
        print("value returned from await:", from_await)

# """
# We're going to create a little class to make a task loop
# """

class TaskLoop():

    def __init__(self):
        # list to hold the tasks
        self.tasks = []

    def add_task(self, task):
        """
        add a task to the loop task must be a coroutine
        """
        self.tasks.append(task)

    def run_all(self):
        """
        This is where the task loop runs
        """
        # Keep a loop going until all the tasks are gone:
        i = 0
        while self.tasks:
            i += 1
            print(f"\nOuter loop count: {i}")
            # pop a task off the end
            task = self.tasks.pop()
            # run that task:
            try:
                res = task.send(None)
                print("result of send:", res)
                # put it back on the beginning of the task list
                self.tasks.insert(0, task)
            except StopIteration:
                # this will be raised if it is done
                # so we don't put it back on the task list
                print("The awaitable is complete")
                # break


print("\n\n*** Running the Loop class\n")

# To use it, we create a task loop object and add tasks to it.

loop = TaskLoop()
loop.add_task(do_a_few_things(2, "first task"))
loop.add_task(do_a_few_things(4, "second task"))
loop.add_task(do_a_few_things(3, "third task"))

# and then call run_all

loop.run_all()

# """
# But remember that the whole point of this is concurrency -- if your tasks all run non-stop 'till they are done, there is no point in all this.
# The point of async is to be able to have multiple tasks running at the same time. This is only useful for tasks that are spending much of their time waiting for something to happen -- like a socket to recieve a message, or a network request to return.

# So let's make a "fake" task that will pause for a bit, before resuming. we can't use a regular time.sleep() call -- as those are blocking, it won't let anythign else run while it's sleeping.

# The asyncio package provides an awaitable sleep, but it turns out that to write it, you need to work with the OS's clock and signals and other deep juju, so we'll make a really simple one:
# """

import time


@coroutine
def sleep(secs=0):
    start = time.time()
    # now we need it to yield control
    yield "{} seconds have passed".format(time.time() - start)
    # and keep yielding it 'till enough time has passed
    while time.time() - start < secs:
        # now we need it to yield control
        yield "yielding in sleep"
    return "{} seconds have passed".format(time.time() - start)

# """
# Now we'll create a little coroutine that calculates something, and pauses a bit with our sleep() coroutine.
# """


async def fib(n):
    """
    Classic fibbonacci number, but with a delay
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    await sleep(1.0)
    return b


# """
# Now that we have a task that returns a value, let's update the task loop to gather the results of the task
# """

class TaskLoop():

    def __init__(self):
        # list to hold the tasks
        self.tasks = []

    def add_task(self, task):
        """
        add a task to the loop task must be a coroutine
        """
        self.tasks.append(task)

    def run_all(self):
        """
        This is where the task loop runs
        """
        # list to hold the results
        results = []

        # Keep a loop going until all the tasks are gone:
        i = 0
        while self.tasks:
            i += 1
            time.sleep(0.001)
            print(f"\nOuter loop count: {i}")
            # pop a task off the end
            task = self.tasks.pop()
            # run that task:
            try:
                res = task.send(None)
                print("returned from send:", res)
                # put it back on the beginning of the task list
                self.tasks.insert(0, task)
            except StopIteration as si:
                # This will be raised if it is done
                # So we don't put it back on the task list
                # Whatever is returned is in the Exception's args
                results.append(si.args[0])
        return results

# """
# Now let's try it out by putting a creating a few tasks and putting them on the loop.
# """

print("\n\n*** Running the Loop with fibbonacci numbers\n")

# Now use it:
loop = TaskLoop()
loop.add_task(fib(3))
loop.add_task(fib(5))
loop.add_task(fib(7))
loop.add_task(fib(10))
loop.add_task(fib(4))
loop.add_task(fib(6))
loop.add_task(fib(9))
loop.add_task(fib(10))

# let's see how long it takes
start = time.time()
results = loop.run_all()
print(f"total run time: {time.time() - start} seconds")

print("the results are:", results)

# """
# let's play around a bit with the time delay and see what happens to the run time.
# """

# """
# Of course, this isn't a very full featured event loop -- you really are better off using one written by the experts in one of teh async packages. but I hope this was a helpful learning exercise -- figuring this out sure helped me better understand async and coroutines!
# """
