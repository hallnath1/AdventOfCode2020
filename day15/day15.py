inputs_nos = [0, 14, 1, 3, 7, 9]

mem = {}
num = int(inputs_nos[-1])
del inputs_nos[-1]

for i, inputs in enumerate(inputs_nos):
    mem[int(inputs)] = i+2

for i in range(len(inputs_nos) + 2, 30000001):
    if num in mem.keys():
        old = num
        num = i - mem[num]
        mem[old] = i
    else:
        mem[num] = i
        num = 0
print(i, num)
