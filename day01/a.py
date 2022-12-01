input = [line.strip() for line in open("day01/input.txt").readlines()]

num_lines = len(input)
kcalMax = 0
kcalSum = 0


for i in range(num_lines):
    if(input[i] != ""):
        kcalSum += int(input[i])
        if kcalSum > kcalMax:
            kcalMax = kcalSum
    else:
        kcalSum = 0
        

print("Highest calories: ", kcalMax)

