

while True:
    try:
        data = input()
        print(f"{data}\t{float(data):.2f}")
    except EOFError:
        break
