import re


def parse_rules(puzzle_input):
    rules = {}

    for line in puzzle_input.splitlines():
        color, contents_text = line.split(' bag contain ')
        items = re.findall(r'(\d+) ([^,]+) bag', contents_text)
        rules[color] = [(int(n), inner) for n, inner in items]

    return rules


file = open('input.txt', 'r').read().replace("bags", "bag")
rules = parse_rules(file)


def count_bags(color):
    return sum(count_bags(rules[inner_color])*x+x for x, inner_color in color)


print(count_bags(rules["shiny gold"]))
