input = [line.strip() for line in open("day01/input.txt").readlines()]

num_lines = len(input)
kcalSum = 0
kcalList = []

for i in range(num_lines):
    if(input[i] != ""):
        kcalSum += int(input[i])
        kcalList.append(kcalSum)
    else:
        kcalSum = 0

kcalListSorted = sorted(kcalList, reverse=True)
print(kcalListSorted[0] + kcalListSorted[1] + kcalListSorted[2])