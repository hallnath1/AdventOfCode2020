import re

checked = set()


def parse_rules(puzzle_input):
    rules = {}

    for line in puzzle_input.splitlines():
        color, contents_text = line.split(' bag contain ')
        items = re.findall(r'(\d+) ([^,]+) bag', contents_text)
        rules[color] = [(int(n), inner) for n, inner in items]

    return rules


def contains(color, rules, target):

    if color in checked:
        return True

    contents = rules[color]

    does_contain = any(
        inner_colour == target or contains(inner_colour, rules, target) for _, inner_colour in contents
    )

    if does_contain:
        checked.add(color)

    return does_contain


def count_containers_of(target, rules):
    count = 0

    for color in rules:
        if contains(color, rules, target):
            count += 1

    return count


file = open('input.txt', 'r').read().replace("bags", "bag")
rules = parse_rules(file)
print(count_containers_of("shiny gold", rules))
