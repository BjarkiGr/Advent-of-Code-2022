#         ___   ___        _  ___          _ 
#        / _ \ / _ \      | |/ _ \        | |
#  _ __ | | | | | | |_ __ | | | | |_ __ __| |
# | '_ \| | | | | | | '_ \| | | | | '__/ _` |
# | |_) | |_| | |_| | |_) | | |_| | | | (_| |
# | .__/ \___/ \___/| .__/|_|\___/|_|  \__,_|
# | |               | |                      
# |_|               |_|
                       
import string
input = [line.strip() for line in open("day03/input.txt").readlines()]

d = dict(zip(string.ascii_letters, range(1, 53)))

totalPoints = 0


def getPriority(x):
    priority = d.get(x)
    return priority

def compare(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] == b[j]):
                return a[i]



for i in range(len(input)):
    rucksack = input[i]
    compA, compB = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    totalPoints += (getPriority((compare(compA, compB))))
        
print(totalPoints)