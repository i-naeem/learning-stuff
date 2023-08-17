

while True:
    try:
        data = input()
        print(f"{float(data):.2f}")
    except EOFError:
        break
