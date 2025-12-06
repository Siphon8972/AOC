import math


def parse_input(filename):
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]

    num_rows = len(lines) - 1
    numbers = []
    for line in lines[:num_rows]:
        numbers.append(list(map(int, filter(None, line.split()))))

    operators = list(filter(None, lines[-1].split()))

    return numbers, operators


def part1(filename):
    numbers, operators = parse_input(filename)
    checksum = 0
    num_problems = len(operators)

    for i in range(num_problems):
        problem_numbers = [row[i] for row in numbers]
        op = operators[i]
        if op == "*":
            checksum += math.prod(problem_numbers)
        elif op == "+":
            checksum += sum(problem_numbers)

    return checksum


def part2(filename):
    numbers, operators = parse_input(filename)
    checksum = 0
    num_problems = len(operators)

    for i in range(num_problems - 1, -1, -1):
        problem_numbers = [row[i] for row in numbers]
        op = operators[i]
        if op == "*":
            checksum += math.prod(problem_numbers)
        elif op == "+":
            checksum += sum(problem_numbers)

    return checksum


print(part1("input.txt"))
print(part2("input.txt"))

