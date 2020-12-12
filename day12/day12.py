import math

instructions = open('input.txt', 'r').read().splitlines()

coord = [0, 0]
angle = 0

compass = {"N": [1, 0], "S": [-1, 0], "E": [0, 1], "W": [0, -1]}
compass_angle = {270: [1, 0], 90: [-1, 0], 0: [0, 1], 180: [0, -1]}

for command in instructions:
    x = command[0]
    val = int(command[1:])
    if x in "NSEW":
        diff = [i*val for i in compass[x]]
        coord = list(map(sum, zip(coord, diff)))
    elif x in "LR":
        angle += val if x == "R" else -val
        angle = angle % 360
    elif x == "F":
        diff = [i*val for i in compass_angle[angle]]
        coord = list(map(sum, zip(coord, diff)))
print("PART A")
print(abs(coord[0])+abs(coord[1]))


def rotate(theta, coord):
    print(theta, coord)
    x, y = coord
    theta = math.radians(theta)
    return [x*math.cos(theta) - y*math.sin(theta), x*math.sin(theta) + y*math.cos(theta)]


waypoint = [1, 10]
coord = [0, 0]

for command in instructions:
    x = command[0]
    val = int(command[1:])
    if x in "NSEW":
        diff = [i*val for i in compass[x]]
        waypoint = list(map(sum, zip(waypoint, diff)))
    elif x in "LR":
        val = val if x == "R" else -val
        waypoint = rotate(val, waypoint)
    elif x == "F":
        diff = [i*val for i in waypoint]
        coord = list(map(sum, zip(coord, diff)))

print("\nPART B")
print(int(abs(coord[0])+abs(coord[1])))
