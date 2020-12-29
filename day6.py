path = "day6.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()


def distinct(answers_of_group):
    seen = set()
    for s in answers_of_group:
        if not s in seen:
            seen.add(s)
    return seen

def intersection(answers_of_persons):
    seen = set()
    for s in answers_of_persons:
        for x in s:
            if x in seen:
                seen.add(x)
    return seen

answers = ''
sum = 0

for i, row in enumerate(data):
    answers = answers + row
    if not row or i == len(data)-1:
        sum = sum + len(distinct(answers))
        answers = ''

union_sum = 0
group = set()

for i, row in enumerate(data):
    if not row or i == len(data)-1:
        union_sum = union_sum + len(intersection(group))
        group.clear()
    else:
        group.add(row)



print('sum of answers (part 1):', sum)
print('sum of answers (part 2):', union_sum)