import csv


def main():
    data = []
    with open("input.txt", "r") as file:
        for line in file:
            data.append(int(line))

    print(partA(data))
    print(partB(data))


def partA(data):
    data.sort()
    for i in range(len(data)):
        j = len(data)-1
        while (data[i]+data[j]) >= 2020:
            if (data[i]+data[j]) == 2020:
                return data[i]*data[j]
            elif data[i]+data[j] > 2020:
                j -= 1
    return 0


def partB(data):
    values = set()
    for i in data:
        for j in values:
            for k in values:
                if i+j+k == 2020:
                    return i*j*k
        values.add(i)


if __name__ == "__main__":
    main()
