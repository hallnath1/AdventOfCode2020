file = open('input.txt', 'r').read().splitlines()


def output(file):
    for line in file:
        print(' '.join(line))


def do_round(file):
    new_file = []
    for i in range(len(file)):
        new_line = []
        for j in range(len(file[i])):
            seat = file[i][j]
            if seat == ".":
                new_line.append(".")
            elif seat == "L":
                if infadjacents([i, j]) == 0:
                    new_line.append("#")
                else:
                    new_line.append("L")
            elif seat == "#":
                if infadjacents([i, j]) >= 5:
                    new_line.append("L")
                else:
                    new_line.append("#")
        new_file.append(new_line)
    return new_file


def check_seats(file, x, y):
    occ = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if x+i > -1 and y+j > -1:
                    if x+i < len(file) and y+j < len(file[0]):
                        if file[x+i][y+j] == "#":
                            occ += 1

    return occ


def infadjacents(pos):
    occupied = 0
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    for i in range(8):
        x, y = pos[1], pos[0]
        while 0 <= x <= len(file[0])-1 and 0 <= y <= len(file)-1:
            x, y = x+dc[i], y+dr[i]
            if 0 <= x <= len(file[0])-1 and 0 <= y <= len(file)-1 and file[y][x] == 'L':
                break
            elif 0 <= x <= len(file[0])-1 and 0 <= y <= len(file)-1 and file[y][x] == '#':
                occupied += 1
                break
    return occupied


def count_seats(file):
    count = 0
    for row in file:
        for seat in row:
            if seat == "#":
                count += 1
    return count


for i in range(100):
    file = do_round(file)

output(file)
print(count_seats(file))
