import re

path = "day4.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()

valid_passprt = 0

pass_fields = {
    "byr": False,
    "iyr": False,
    "eyr": False,
    "hgt": False,
    "hcl": False,
    "ecl": False,
    "pid": False,
}

for i, line in enumerate(data):
    match = re.findall(r'([a-z]{3}):.+?', line)
    if(len(match) == 0):
        for k, v in pass_fields.items():
            pass_fields[k] = False
    else:
        for m in match:
            if(m != "cid"):
                pass_fields[m] = True
        
        if(all(x for x in pass_fields.values())):
            valid_passprt += 1
            for k, v in pass_fields.items():
                pass_fields[k] = False
    print(match)
    print(pass_fields)

print('valid pass:', valid_passprt)
