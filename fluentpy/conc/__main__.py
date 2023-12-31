import sys
import mlp
import time
import sync
import thread

mode = None
try:
    mode = sys.argv[1]
except IndexError:
    pass

SITES = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 10

start_time = time.perf_counter()

if mode == 's':  # Synchronize Version
    sync.download_all_sites(sites=SITES)
elif mode == 't':  # Threading Version
    thread.download_all_sites(sites=SITES)
elif mode == 'm':  # Multiprocessing Version
    mlp.download_all_sites(SITES)
elif mode == 'a':  # Async Version
    pass

else:
    print('No Mode Selected')


duration = time.perf_counter() - start_time
print(f"Downloaded {len(SITES)} in {duration} seconds")
