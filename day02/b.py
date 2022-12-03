#         ___   ___        _  ___          _ 
#        / _ \ / _ \      | |/ _ \        | |
#  _ __ | | | | | | |_ __ | | | | |_ __ __| |
# | '_ \| | | | | | | '_ \| | | | | '__/ _` |
# | |_) | |_| | |_| | |_) | | |_| | | | (_| |
# | .__/ \___/ \___/| .__/|_|\___/|_|  \__,_|
# | |               | |                      
# |_|               |_|                      

totalPoints = 0
opponent = []
myself = []

win = 6
draw = 3
loss = 0

rock = 1
paper = 2
scissors = 3


file = open("day02/input.txt","r")
for line in file:
    x, y = line.split(' ', 1)
    opponent.append(x)
    myself.append(y.replace("\n", ""))


for i in range(len(myself)):
    if(myself[i] == "X"):
        totalPoints += loss
        if(opponent[i] == "A"):
            totalPoints += scissors
        elif(opponent[i] == "B"):
            totalPoints += rock
        elif(opponent[i] == "C"):
            totalPoints += paper

    elif(myself[i] == "Y"):
        totalPoints += draw
        if(opponent[i] == "A"):
            totalPoints += rock
        elif(opponent[i] == "B"):
            totalPoints += paper
        elif(opponent[i] == "C"):
            totalPoints += scissors

    elif(myself[i] == "Z"):
        totalPoints += win
        if(opponent[i] == "A"):
            totalPoints += paper
        elif(opponent[i] == "B"):
            totalPoints += scissors
        elif(opponent[i] == "C"):
            totalPoints += rock


print(totalPoints)