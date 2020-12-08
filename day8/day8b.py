lines = open('input.txt', 'r').read().splitlines()
program = list(map(lambda x: x.split(' '), lines))

for i in range(len(program)):
    if program[i][0] == "nop":
        program[i][0] = "jmp"
    elif program[i][0] == "jmp":
        program[i][0] = "nop"

    seen = set()
    acc = 0
    pc = 0

    while pc < len(program):

        opcode = program[pc][0]
        operand = int(program[pc][1])
        #print(pc, ":", opcode, operand)

        if pc in seen:
            break
        seen.add(pc)

        if opcode == 'jmp':
            pc += operand
            continue
        elif opcode == 'acc':
            acc += operand
        elif opcode == 'nop':
            pass
        pc += 1
    if pc > 611:
        print(acc)
        print(pc)
        print(i+1)

    if program[i][0] == "nop":
        program[i][0] = "jmp"
    elif program[i][0] == "jmp":
        program[i][0] = "nop"
