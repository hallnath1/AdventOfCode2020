import re
KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

file = open('input.txt', 'r')
allPassports = file.read().split('\n\n')


def cleanPassport(p):
    pairs = [(k, v) for (k, v) in [row.split(':')
                                   for row in [row for row in re.split('[\n|\s]', p)]]]
    return pairs


def check(passport):
    keysInThisPassPort = [pair[0] for pair in passport]
    for key in KEYS:
        if key not in keysInThisPassPort:
            return False

    return True


def verify(passport):
    keyChecks = {
        'byr': lambda v: int(v) >= 1920 and int(v) <= 2002,
        'iyr': lambda v: int(v) >= 2010 and int(v) <= 2020,
        'eyr': lambda v: int(v) >= 2020 and int(v) <= 2030,
        'hgt': lambda v: bool(re.match("^(1[5-8][0-9]|19[0-3])(cm)$|^(59|6[0-9]|7[0-6])(in)$", v)),
        'hcl': lambda v: bool(re.match('^#([0-9]|[a-f]){6}$', v)),
        'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v: bool(re.match("^[0-9]{9}$", v)),
        'cid': lambda v: True if v else True
    }
    for pair in passport:
        k = pair[0]
        v = pair[1]
        if not keyChecks[k](v):
            return False

    return True


cleanedPassports = [cleanPassport(p) for p in allPassports]
cleanedPassports = [p for p in cleanedPassports if check(p)]
cleanedPassports = [p for p in cleanedPassports if verify(p)]

print(len(list(cleanedPassports)))
