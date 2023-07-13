
tels = [
    (92, 3581),
    (333, 5674),
    (11, 'asdf'),
    (3333),
    (333, 'A'),
    (92),
]

for tel in tels:
    match tel:
        case [int(a), str(b)]:
            print('First')

        case [int(a), int(b)]:
            print('Second')

        case a:
            print('Third')
