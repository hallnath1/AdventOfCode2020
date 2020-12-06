file = open('input.txt', 'r').read()
file = [x for x in file.split("\n")]

groups = []
group = ""
for line in file:
    if line == "":
        groups.append(set(group))
        group = ""
    else:
        group += line
groups.append(set(group))

print("Part A:", sum(map(len, groups)))

alpha = "abcdefghijklmnopqrstuvwxyz"
count = 0
group = set(alpha)
for line in file:
    if line == "":
        count += len(group)
        group = set(alpha)
    else:
        group = group & set(line)

count += len(group)

print("Part B:", count)
