import time
import os


def child(pipe_out):
    zzz = 0
    while True:
        time.sleep(zzz)
        message = "Spam {zzz:03}".encode()
        os.write(pipe_out, message)
        zzz = (zzz + 1) % 5


def parent():
    pipe_in, pipe_out = os.pipe()

    if os.fork() == 0:
        child(pipe_out)

    else:
        while True:
            line = os.read(pipe_in, 32)
            print(f'Parent {os.getpid()} got [{line}] at {time.time()}')
