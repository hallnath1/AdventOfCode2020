import math
r = open('input.txt', 'r').read()
input = [x.split(' = ') for x in r.splitlines()]

# Part 1
mask = ''
mem = {}
for line in input:
    if line[0] == 'mask':
        mask = line[1]
    else:
        key = int(line[0][4:-1])
        data = int(line[1])
        output = ""
        for x in range(36):
            next = mask[35-x]
            if next == 'X':
                next = str(data % 2)
            output = next + output
            data = data//2
        mem[key] = output

sum = 0
for key in mem:
    sum = sum + int(mem[key], 2)

print(sum)

# Part 2
mask = ''
mem = {}
for line in input:
    if line[0] == 'mask':
        mask = line[1]
    else:
        key = int(line[0][4:-1])
        data = int(line[1])
        floating = []
        target = ''
        for x in range(36):
            next = mask[35-x]
            if next == '0':
                next = str(key % 2)
            if next == 'X':
                floating.append(35-x)
            target = next + target
            key = key//2
        for i in range(0, int(math.pow(2, len(floating)))):
            for index in floating:
                target = target[:index] + str(i % 2) + target[index+1:]
                i = i//2
            mem[int(target)] = data

sum = 0
for key in mem:
    sum = sum + mem[key]

print(sum)
