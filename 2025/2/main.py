def pattern(x):
    Homogeneous = False
    iter = 0
    while (not Homogeneous) and (iter <= len(str(x)) / 2):
        y = str(x)[0:iter]
        print(y)
        if str(x).replace(y, "") == "":
            Homogeneous = True
        iter += 1
    return Homogeneous

with open("./input.txt", "r") as f:
    f = f.readline()

f = f.split(",")
n = []
num = 0


for i in range(len(f)):
    f[i] = f[i].replace("\n", "")
    n.append(f[i].split("-"))

for i in range(len(n)):
    val = n[i][0]
    for x in range(abs(int(n[i][0]) - int(n[i][1]))):
        if pattern((x + int(n[i][0]))):
            num = num + x + int(n[i][0])

print(num)
