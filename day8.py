path = "day8.txt"
data_file = open(path, 'r')

import re

accu = 0
dup_found = False
i = 0

data = data_file.read().splitlines()

exec_table = []

def parse_statement(str):
    m = re.match(r'(nop|acc|jmp) ([\+\-]\d+)', str)
    return (m.group(1), m.group(2), 0)

for statement in data:
    exec_table.append(parse_statement(statement))

while dup_found == False:
    statement = exec_table[i]
    if(statement[2] > 0):
        dup_found = True
        break

    exec_table[i] = (statement[0], statement[1], statement[2] + 1)
    comm = statement[0]
    if comm == 'nop':
        i = i + 1
    if comm == 'acc':
        accu = accu + int(statement[1])
        i = i + 1
    if comm == 'jmp':
        i = i + int(statement[1])

print(accu)