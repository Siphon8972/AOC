from io import StringIO
import time


def HighJoltage(x):
    count = 0
    y = [-1, 0]
    z = [-1, 0]
    while count < len(x) - 1:
        if int(x[count]) > y[0]:
            y[0] = int(x[count])
            y[1] = count
        count += 1
    count = y[1] + 1
    while count < len(x):
        if int(x[count]) >= z[0]:
            z[0] = int(x[count])
            z[1] = count
        count += 1
    return int(str(y[0]) + str(z[0]))


def HighJoltage2(x):
    n = len(x)
    CountRemove = n - 12
    result = []
    for digit in x:
        while CountRemove > 0 and result and result[-1] < digit:
            result.pop()
            CountRemove -= 1
        result.append(digit)
    final_digits = result[:12]
    return int("".join(final_digits))


test = StringIO("""987654321111111
811111111111119
234234234234278
818181911112111
""")
sum = 0

with open("./input.txt", "r") as f:
    x = f.readlines()

x = [s.replace("\n", "") for s in x]

start = time.time()

for i in range(len(x)):
    result = HighJoltage2(x[i])
    sum += result


print("This took", time.time() - start, "seconds")
print(sum)
