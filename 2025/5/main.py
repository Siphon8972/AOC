from io import StringIO
import time


def Part1(ranges, values):
    count = 0
    for x in values:
        for i in ranges:
            if x >= i[0] and x <= i[1]:
                count += 1
                break
    return count


def Part2(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])

    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return sum(end - start + 1 for start, end in merged)


x = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

with open("./input.txt", "r") as f:
    # with StringIO(x) as f:
    ranges = []
    values = []
    x = f.readline()
    while x != "\n":
        ranges.append(x)
        x = f.readline()
    x = f.readline()
    while x != "":
        values.append(x)
        x = f.readline()

ranges = list(map(lambda x: x.replace("\n", ""), ranges))
ranges = list(map(lambda x: x.split("-"), ranges))
ranges = list(map(lambda x: list(map(int, x)), ranges))

values = list(map(lambda x: x.replace("\n", ""), values))
values = list(map(int, values))

print(Part2(ranges))
print(time.process_time())
