# Positional Arguments Only Function
def positional_only(a, b, /, c=1):
    print(a, b, c)


positional_only(1, 2, c=2)
