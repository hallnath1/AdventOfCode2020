def slopeCheck(grid, xCount, yCount):
    x = 0
    y = 0
    count = 0
    while len(grid) > y:
        if x >= len(grid[0]):
            x -= len(grid[0])

        if grid[y][x] == "#":
            count += 1

        x += xCount
        y += yCount
    return count


grid = []
with open('input.txt') as file:
    for line in file:
        line = list(line.strip('\n'))
        grid.append(line)


print("Part A")
print(slopeCheck(grid, 3, 1))

print("Part B")
print(slopeCheck(grid, 1, 1)*slopeCheck(grid, 3, 1) *
      slopeCheck(grid, 5, 1)*slopeCheck(grid, 7, 1)*slopeCheck(grid, 1, 2))
