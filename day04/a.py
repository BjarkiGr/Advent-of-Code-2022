#         ___   ___        _  ___          _
#        / _ \ / _ \      | |/ _ \        | |
#  _ __ | | | | | | |_ __ | | | | |_ __ __| |
# | '_ \| | | | | | | '_ \| | | | | '__/ _` |
# | |_) | |_| | |_| | |_) | | |_| | | | (_| |
# | .__/ \___/ \___/| .__/|_|\___/|_|  \__,_|
# | |               | |
# |_|               |_|

a = []
b = []

taskAA = []
taskAB = []
taskBA = []
taskBB = []

counter = 0
nacounter = 0

input = open("day04/input.txt", "r")
for group in input:
    x, y = group.split(',', 1)
    a.append(x)
    b.append(y)


for i in range(len(a)):
    m, n = a[i].split('-', 1)
    o, p = b[i].split('-', 1)
    taskAA.append(m)
    taskAB.append(n)
    taskBA.append(o)
    taskBB.append(p)

for i in range(len(a)):
    if taskAA[i] <= taskBA[i] and taskAB[i] >= taskBB[i]:
        counter += 1
        print("A includes B")

    elif taskAA[i] >= taskAB[i] and taskAB[i] <= taskBB[i]:
        counter += 1
        print("B includes A")

    elif taskBA[i] <= taskAA[i] and taskBB[i] >= taskAB[i]:
        counter += 1
        print("B includes A")

    else:
        nacounter += 1
        print("n/a")
        print(taskAA[i], taskAB[i], taskBA[i], taskBB[i])




print(counter, "are fully included")
print(nacounter, "are not included")
