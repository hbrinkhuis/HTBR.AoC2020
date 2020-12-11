import re

path = "day4.txt"
data_file = open(path, 'r')

data = data_file.read().splitlines()

def from_to(x,fr,to):
    return x.isdigit() and int(x) >= fr and int(x) <= to

def height_validation(hgt):
    m = re.match(r'(\d{2,3})(cm|in)', hgt)
    if(m):
        size = m.group(1)
        unit = m.group(2)
        if(unit == "cm"):
            return from_to(size, 150, 193)
        if(unit == "in"):
            return from_to(size, 59, 76)
    return False

pass_evals = {
    "byr": lambda x: from_to(x, 1920, 2002),
    "iyr": lambda x: from_to(x, 2010, 2020),
    "eyr": lambda x: from_to(x, 2020, 2030),
    "hgt": lambda x: height_validation(x),
    "hcl": lambda x: re.match(r'#[0-9a-f]{6}', x),
    "ecl": lambda x: re.match(r'amb|blu|brn|gry|grn|hzl|oth', x),
    "pid": lambda x: bool(re.match(r'^\d{9}$', x))
}

def find_valids(validate_fields):
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
        match = re.findall(r'([a-z]{3}):([\w#]+)', line)
        if(len(match) == 0):
            for k in pass_fields.keys():
                pass_fields[k] = False
        else:
            for i, val in match:
                if(i != "cid"):
                    pass_fields[i] = pass_evals[i](val) if validate_fields else True
            
            if(all(x for x in pass_fields.values())):
                valid_passprt += 1
                for k in pass_fields.keys():
                    pass_fields[k] = False
        
    return valid_passprt


print('valid pass:', find_valids(False))
print('valid pass pt 2:', find_valids(True))