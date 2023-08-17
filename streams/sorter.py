writer_data = []
reader_data = []
sorted_data = []


while True:
    try:
        tb = input()
        [w, r] = tb.split('\t')
        writer_data.append(w)
        reader_data.append(r)
        sorted_data.append(r)
    except EOFError:
        break

for w, r, s in zip(writer_data, reader_data, sorted(sorted_data)):
    print(w, r, s, sep="\t")
