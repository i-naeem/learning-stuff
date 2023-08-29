import time
import os


def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        message = "Spam {zzz:03}".encode()
        os.write(pipeout, message)
        zzz = (zzz + 1) % 5


def parent():
    pipein, pipeout = os.pipe()

    if os.fork() == 0:
        child(pipeout)

    else:
        while True:
            line = os.read(pipein, 32)
            print(f'Parent {os.getpid()} got [{line}] at {time.time()}')
