import stdfuns

values = stdfuns.open_file_lines('day1.txt')

# convert to int
intvalues = sorted(list(map(lambda x: int(x), values)))

print('calculating part 1...')
found = False
for x in intvalues:
    for y in intvalues[::-1]:
        if x + y == 2020:
            print('found pair!', x, y)
            print('answer is:', x * y)
            found = True
            break
        if x + y < 2020:
            break
    if found:
        break

print('calculating part 2...')
found = False
for i, x in enumerate(intvalues):
    for y in intvalues[i::]:
        for z in intvalues[::-1]:
            if x + y + z == 2020:
                print('found triplet!', x, y, z)
                print('answer is:', x * y * z)
                found = True
            if z <= y:
                break
        if found:
            break
    if found:
        break
