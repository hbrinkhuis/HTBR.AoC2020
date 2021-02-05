import stdfuns

data = stdfuns.open_file_split('day6.txt')

def distinct(answers_of_group):
    seen = set()
    for s in answers_of_group:
        if not s in seen:
            seen.add(s)
    return seen

def intersects(answers_of_group):
    seen = set()
    for i, s in enumerate(answers_of_group):
        if i == 0:
            seen = s
            next
        seen = seen & s
    return seen

answers = ''
sum = 0

for i, row in enumerate(data):
    answers = answers + row
    if not row or i == len(data)-1:
        sum = sum + len(distinct(answers))
        answers = ''

union_sum = 0
group = []

for i, row in enumerate(data):
    if not row or i == len(data)-1:
        union_sum = union_sum + len(intersects(group))
        group.clear()
    else:
        group.append(set(row))

print('sum of answers (part 1):', sum)
print('sum of answers (part 2):', union_sum)