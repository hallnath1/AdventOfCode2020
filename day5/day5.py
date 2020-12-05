seats = []

file = open('input.txt', 'r').read()
file = [x for x in file.split("\n")]
answer = 0
for line in file:
    line = line.strip('\n')

    f = 0
    b = 127
    for command in line[:7]:
        if command == "F":
            b = (f+b)//2
        elif command == "B":
            f = (f+b)//2 + 1
    row = b

    l = 0
    r = 7

    for command in line[7:]:
        if command == "L":
            r = (l+r)//2
        elif command == "R":
            l = (l+r)//2 + 1
    col = r
    seats.append(row*8+col)
    answer = max(answer, row*8+col)

all_seats = set([x for x in range(992)])
print(all_seats - set(seats))
print(answer)
# for x in range(1024):
#     if x not in seats:
#         print(x)
