import math

f = open("ex1input.txt","r")

sum = 0
partSum = 0

for line in f:
    partSum = math.floor(int(line) / 3) - 2
    sum += partSum

    while (math.floor(partSum / 3) - 2) >= 0:
        partSum = math.floor(partSum / 3) - 2
        sum += partSum

print('Sum is:', sum)

