countA = 0
countB = 0

with open('input.txt') as file:
    for line in file:
        lineList = line.strip("\n").split(" ")

        policy = lineList[0].split("-")
        min = int(policy[0])
        max = int(policy[1])

        character = lineList[1][0]

        charCount = lineList[2].count(character)

        if charCount >= min and charCount <= max:
            countA += 1

        if bool(lineList[2][min-1] == character) != bool(lineList[2][max-1] == character):
            countB += 1

print("Part A")
print(countA)

print("Part B")
print(countB)
