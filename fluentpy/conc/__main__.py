import sys
import time
import sync
import thread

mode = sys.argv[1]

SITES = [
    "https://www.jython.org",
    "http://olympus.realpython.org/dice",
] * 10

start_time = time.perf_counter()

if mode == 's':  # Synchronize Version
    sync.download_all_sites(sites=SITES)
elif mode == 't':  # Threading Version
    thread.download_all_sites(sites=SITES)
elif mode == 'a':  # Async Version
    pass


duration = time.perf_counter() - start_time
print(f"Downloaded {len(SITES)} in {duration} seconds")
