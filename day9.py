import stdfuns

data = stdfuns.open_file_split('day9.txt')

preamble_len = 5

for i, n in enumerate(data[preamble_len:], 5):
    # no doubles!
    print(i, n)
