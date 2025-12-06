from itertools import zip_longest
from io import StringIO


def cephalopod_math_from_lines(lines):
    lines = [line.rstrip("\n") for line in lines]
    number_rows, operator_row = lines[:-1], lines[-1]
    n_rows = len(number_rows)
    n_cols = max(len(line) for line in lines)

    number_rows = [line.ljust(n_cols) for line in number_rows]
    operator_row = operator_row.ljust(n_cols)

    columns = [[number_rows[r][c] for r in range(n_rows)] for c in range(n_cols)]
    operators = list(operator_row)

    problems = []
    current_cols = []
    current_ops = []
    for col, op in zip(columns, operators):
        if all(ch == " " for ch in col):
            if current_cols:
                problems.append((current_cols, current_ops))
                current_cols, current_ops = [], []
        else:
            current_cols.append(col)
            current_ops.append(op)
    if current_cols:
        problems.append((current_cols, current_ops))

    total_sum = 0
    for cols, ops in reversed(problems):  # right-to-left
        operator = next((o for o in reversed(ops) if o != " "), None)
        numbers = [int("".join(col).strip()) for col in cols if "".join(col).strip()]
        if operator == "+":
            result = sum(numbers)
        elif operator == "*":
            result = 1
            for n in numbers:
                result *= n
        else:
            raise ValueError(f"Unknown operator: {operator}")
        total_sum += result

    return total_sum


x = """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +"""


#   with StringIO(x) as f:
with open("input.txt") as f:
    lines = f.readlines()

print(cephalopod_math_from_lines(lines))

