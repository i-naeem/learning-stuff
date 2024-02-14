
TEXT_FILE = "./file.txt"

with open(TEXT_FILE, mode='r', encoding="utf-8") as f:
    print(dir(f))
