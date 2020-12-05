count = 0
with open('input.txt') as file:
    passportKey = []
    for line in file:
        if line == "\n":
            if set([
                "byr",
                "iyr",
                "eyr",
                "hgt",
                "hcl",
                "ecl",
                "pid",
            ]).issubset(set(passportKey)):
                count += 1
            passportKey = []
        else:
            line = line.strip("\n").split(" ")
            for part in line:
                part = part.split(":")
                passportKey.append(part[0])
    if set([
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]).issubset(set(passportKey)):
        count += 1

print(count)
