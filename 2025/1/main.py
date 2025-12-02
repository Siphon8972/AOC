with open("./input.txt", "r") as r:
    x = r.readlines()
for i in range(len(x)):
    x[i] = x[i].replace("\n", "")

val = 50
count = 0
for i in range(len(x)):
    if x[i][0] == "R":
        for z in range(int(x[i][1:])):
            val += 1
            val %= 100
            if val == 0:
                count += 1
    else:
        for z in range(int(x[i][1:])):
            val -= 1
            val %= 100
            if val == 0:
                count += 1
print(count)
