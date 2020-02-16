
f = open("ex2input.txt","r")
opCode = f.read().split(',')
opCode = list(map(int, opCode))
print('input: ', opCode)

verbResult = None
nounResult = None
i = 0
for noun in range(99):
    for verb in range(99):
        testOpCode = opCode.copy()
        testOpCode[1] = noun
        testOpCode[2] = verb
        #print('test:', testOpCode)

        while i < len(testOpCode):
            part = testOpCode[i:i+4]
            #print('it: ', i, 'part: ', part)

            if testOpCode[i] == 1:
                testOpCode[testOpCode[i+3]] = testOpCode[testOpCode[i+1]] + testOpCode[testOpCode[i+2]]

            elif testOpCode[i] == 2:
                testOpCode[testOpCode[i + 3]] = testOpCode[testOpCode[i + 1]] * testOpCode[testOpCode[i + 2]]

            elif testOpCode[i] == 99:
                if testOpCode[0] == 19690720:
                    verbResult = verb
                    nounResult = noun
                i = 0
                break

            i += 4



print('result: ', nounResult, verbResult)