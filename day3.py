path = "day3.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()

rows = len(data)
columns = len(data[0])

print(rows, "rows and", columns, "columns")

matrix = [[i for i in j] for j in data]

trees = 0
column_index = 0
for i, row in enumerate(matrix):
    if row[column_index] == '#':
        trees  += 1

    column_index += 3
    if(column_index >= columns):
        column_index = column_index - columns

print('Number of trees:', trees, '(part 1)')