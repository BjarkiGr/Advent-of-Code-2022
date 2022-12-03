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
        totalPoints += rock
        if(opponent[i] == "A"):
            totalPoints += draw
        elif(opponent[i] == "B"):
            totalPoints += loss
        elif(opponent[i] == "C"):
            totalPoints += win

    elif(myself[i] == "Y"):
        totalPoints += paper
        if(opponent[i] == "A"):
            totalPoints += win
        elif(opponent[i] == "B"):
            totalPoints += draw
        elif(opponent[i] == "C"):
            totalPoints += loss

    elif(myself[i] == "Z"):
        totalPoints += scissors
        if(opponent[i] == "A"):
            totalPoints += loss
        elif(opponent[i] == "B"):
            totalPoints += win
        elif(opponent[i] == "C"):
            totalPoints += draw


print(totalPoints)