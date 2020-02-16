import math

f = open("ex1input.txt","r")

sum = 0

for line in f:
    sum = sum + math.floor(int(line) / 3) - 2

print('Sum is:', sum)

