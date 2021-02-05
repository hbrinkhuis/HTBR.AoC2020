import math
import stdfuns

data = stdfuns.open_file_split('day3.txt')

rows = len(data)
columns = len(data[0])

matrix = [[i for i in j] for j in data]

def traverse(right, down):
    trees = 0
    for i, val in enumerate(range(0, rows, down)):
        if matrix[val][(i*right) % columns] == '#':
            trees  += 1

    return trees

print('Number of trees:', traverse(3,1), '(part 1)')

trees = list(map(traverse, (1,3,5,7,1), (1,1,1,1,2)))
print('Product of number of trees:', math.prod(trees), '(part 2)')