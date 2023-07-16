# Positional Arguments Only Function
from operator import methodcaller


def positional_only(a, b, /, c=1):
    print(a, b, c)


positional_only(1, 2, c=2)


hyphenate = methodcaller('replace', ' ', '_')
to_lowercase = methodcaller('lower')
# joiner = methodcaller('join', ' ')


dt = ['Audrey McCullen', 'Mark Wood', 'Steve Smith']


for n in dt:
    print(to_lowercase(hyphenate(n)))
