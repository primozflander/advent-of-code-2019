def checkPar(x):
    if x == "":
        return "0"
    else:
        return x

f = open("ex5input.txt","r")
testOpCode = f.read().split(',')
testOpCode = list(map(int, testOpCode))
print("input: ", testOpCode)
print("lenght of input:", len(testOpCode))

#testOpCode = [3,0,4,0,99]

i = 0
while i < len(testOpCode):

    # slice opCode
    print('opCode: ', testOpCode[i])
    opCode = str(testOpCode[i])
    instruction = opCode[-2:]
    if len(instruction) < 2:
        instruction = "0" + instruction
    print("instruction: ", instruction)
    par1 = checkPar(opCode[-3:-2])
    print("par1: ", par1)
    par2 = checkPar(opCode[-4:-3])
    print("par2: ", par2)
    par3 = checkPar(opCode[-5:-4])
    print("par3: ", par3)

    # sum
    if instruction == "01":
        if par1 == "0":
            firstPar = testOpCode[testOpCode[i + 1]]
        else:
            firstPar = testOpCode[i + 1]
        print("firstPar: ", firstPar)
        if par2 == "0":
            secondPar = testOpCode[testOpCode[i + 2]]
        else:
            secondPar = testOpCode[i + 2]
        print("secondPar: ", secondPar)
        testOpCode[testOpCode[i + 3]] = int(firstPar) + int(secondPar)
        print(int(firstPar) + int(secondPar))
        i += 4

    # multiply
    elif instruction == "02":
        if par1 == "0":
            firstPar = testOpCode[testOpCode[i + 1]]
        else:
            firstPar = testOpCode[i + 1]
        print("firstPar: ", firstPar)
        if par2 == "0":
            secondPar = testOpCode[testOpCode[i + 2]]
        else:
            secondPar = testOpCode[i + 2]
        print("secondPar: ", secondPar)
        testOpCode[testOpCode[i + 3]] = int(firstPar) * int(secondPar)
        i += 4

    # input
    elif instruction == "03":
        if par1 == "0":
            print("before", testOpCode[testOpCode[i + 1]])
            testOpCode[testOpCode[i + 1]] = input("Input ID (Address): ")
            print("after", testOpCode[testOpCode[i + 1]])
        else:
            print("before", testOpCode[i + 1])
            testOpCode[i + 1] = input("Input ID: ")
            print("after", testOpCode[i + 1])
        i += 2

    # output
    elif instruction == "04":
        if par1 == "0":
            print("final result (Address): ", testOpCode[testOpCode[i + 1]])
        else:
            print("final result: ", testOpCode[i + 1])
        i += 2
    # end
    elif instruction == "99":
        print("Done!")
        break

    # error
    else:
        print("Error")
        break