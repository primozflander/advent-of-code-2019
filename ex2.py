
f = open("ex2input.txt","r")
testOpCode = f.read().split(',')
testOpCode = list(map(int, testOpCode))
print(testOpCode)

testOpCode[1] = 12
testOpCode[2] = 2
print(testOpCode)

#testOpCode = [1,1,1,4,99,5,6,0,99]

i = 0
while i < len(testOpCode):
    part = testOpCode[i:i+4]
    print('part: ', part)

    if testOpCode[i] == 1:
        testOpCode[testOpCode[i+3]] = testOpCode[testOpCode[i+1]] + testOpCode[testOpCode[i+2]]

    elif testOpCode[i] == 2:
        testOpCode[testOpCode[i + 3]] = testOpCode[testOpCode[i + 1]] * testOpCode[testOpCode[i + 2]]

    elif testOpCode[i] == 99:
        break

    i += 4

print('result: ', testOpCode)