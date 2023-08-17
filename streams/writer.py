import sys
from random import random

rng = 10
try:
    rng = int(sys.argv[-1])
except ValueError:
    pass

for _ in range(int(rng)):
    print(random())
