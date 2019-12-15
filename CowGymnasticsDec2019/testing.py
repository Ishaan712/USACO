someArr = []
variables = []
with open("gymnastics.in") as f:
    for line in f:
        numbers_str = line.split()
        #convert numbers to floats
        numbers_float = [int(x) for x in numbers_str]
        for i in numbers_float:
            someArr.append(i)



variables.append(someArr[0])
variables.append(someArr[1])
print(someArr)
someArr.remove(someArr[0])
someArr.remove(someArr[0])
print(someArr)

sessions = variables[0]
numofcows = variables[1]

cowsbysessions = [[[" " for k in range(numofcows)] for j in range(1)] for i in range(sessions)]

k = 0
for x in range(0, sessions):
    for i in range(0, numofcows):
        cowsbysessions[x][0][i] = someArr[k]
        k = k + 1


