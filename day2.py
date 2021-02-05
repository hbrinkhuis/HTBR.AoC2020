import re
import stdfuns

values = stdfuns.open_file_lines('day2.txt')

num_valid_part_1 = 0
num_valid_part_2 = 0
for v in values:
    match = re.search(r'(\d+)-(\d+) ([a-z]+): ([a-z]+)', v)
    min_char = int(match[1])
    max_char = int(match[2])
    char = match[3]
    passwd = match[4]
    occurences = len(re.findall(char, passwd))
    if occurences >= min_char and occurences <= max_char:
        num_valid_part_1 += 1
    
    chrlist = list(passwd)
    indices = [i + 1 for i, value in enumerate(chrlist) if value == char]
    if (min_char in indices) ^ (max_char in indices):
        num_valid_part_2 += 1

print(num_valid_part_1, "are valid (part 1)")
print(num_valid_part_2, "are valid (part 2)")