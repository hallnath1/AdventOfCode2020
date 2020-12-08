lines = open('input.txt', 'r').read().splitlines()
program = list(map(lambda x: x.split(' '), lines))

seen = set()

acc = 0
pc = 0
while pc < len(program):
    if pc in seen:
        break
    seen.add(pc)
    opcode = program[pc][0]
    operand = int(program[pc][1])
    if opcode == 'jmp':
        pc += operand
        continue
    elif opcode == 'acc':
        acc += operand
    elif opcode == 'nop':
        pass
    pc += 1

print(acc)
