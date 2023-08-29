import os
import time
import threading


def child(pipe_out):
    zzz = 0
    while True:
        time.sleep(zzz)
        message = "Spam {}".format(zzz).encode()
        os.write(pipe_out, message)
        zzz = (zzz + 1) % 5


def parent(pipe_in):
    while True:
        line = os.read(pipe_in, 32)
        print(f"Parent {os.getpid()} got {line} at {time.time()}")


pipe_in, pipe_out = os.pipe()
threading.Thread(target=child, args=(pipe_out,)).start()
parent(pipe_in)
