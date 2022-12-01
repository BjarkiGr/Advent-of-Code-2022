input = [line.strip() for line in open('input.txt').readlines()]

num_lines = len(input)
kcalMax = 0
kcal2nd = 0
kcal3rd = 0
kcalSum = 0


for i in range(num_lines):
    if(input[i] != ""):
        kcalSum += int(input[i])
        if kcalSum > kcalMax:
            kcalMax = kcalSum
        elif kcalSum > kcal2nd and kcalSum < kcalMax:
            kcal2nd = kcalSum
        elif kcalSum > kcal3rd and kcalSum < kcalMax and kcalSum < kcal2nd:
            kcal3rd = kcalSum
    else:
        kcalSum = 0

print("1st: ", kcalMax)
print("2nd: ", kcal2nd)
print("3rd: ", kcal3rd)
print("Top 3 sum: ", kcalMax + kcal2nd + kcal3rd)
