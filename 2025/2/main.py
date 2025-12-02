def pattern(x):
    Homogeneous = False
    iter = 1
    while (not Homogeneous) and (iter <= len(str(x)) // 2):
        y = str(x)[0:iter]
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
    val = int(n[i][0])
    while val <= int(n[i][1]):
        if pattern(val):
            num += val
        val += 1
print(num)
