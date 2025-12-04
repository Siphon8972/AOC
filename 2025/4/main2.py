from io import StringIO
from collections import defaultdict
import time


def Surroundingat(coords, pos):
    count = 0
    for vect in (
        (0 + 1j),
        (1 + 1j),
        (1 + 0j),
        (1 - 1j),
        (0 - 1j),
        (-1 - 1j),
        (-1 - 0j),
        (-1 + 1j),
    ):
        ppos = pos + vect
        if coords[ppos] == "@":
            count += 1
    return count


x = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

coords = defaultdict(lambda: ".")

with open("./input.txt", "r") as f:
    # with StringIO(x) as f:
    fp = f.read().strip()
    lines = fp.splitlines()
    for y, string in enumerate(lines):
        for x, chr in enumerate(string):
            if chr == "@":
                coords[complex(x, y)] = chr

GridWidth = len(lines[0])
GridHeight = len(lines)

finalcount = 0
modified = True
while modified:
    modified = False
    for i in range(GridWidth):
        for x in range(GridHeight):
            cordinate = complex(i, x)
            if coords[cordinate] == "@":
                if Surroundingat(coords, cordinate) < 4:
                    modified = True
                    finalcount += 1
                    coords.pop(cordinate)
print(finalcount)
print("It took", time.process_time(), "seconds to complete")
