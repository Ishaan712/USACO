consistencies = 0

someArr = []
variables = []
with open("gymnastics.in") as f:
    for line in f:
        numbers_str = line.split()
        numbers_int = [int(x) for x in numbers_str]
        for i in numbers_int:
            someArr.append(i)


variables.append(someArr[0])
variables.append(someArr[1])
someArr.remove(someArr[0])
someArr.remove(someArr[0])

sessions = variables[0]
numofcows = variables[1]

cowsbysessions = [[[" " for k in range(numofcows)] for j in range(1)] for i in range(sessions)]

k = 0
for x in range(0, sessions):
    for i in range(0, numofcows):
        cowsbysessions[x][0][i] = someArr[k]
        k = k + 1

def makeArray(a):
    cowNumbers = []
    for x in range(0, numofcows):
        cowNumbers.append(cowsbysessions[a][0][x])
    return cowNumbers

# remove unique
def checkio(data):
    for index in range(len(data) - 1, -1, -1):
        if data.count(data[index]) == 1:
            del data[index]
    return data


# count how many times duplicates occur
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

def findConsistency(consistencies, tempX):
    arrayForIndex = []
    temp = (makeArray(0)[tempX])
    for j in range(0, sessions):
        for y in range(1, numofcows):
            makeArray(j)
            if makeArray(j).index(temp) < makeArray(j).index(makeArray(j)[y]):
                arrayForIndex.append(makeArray(j)[y])

    arrayForIndex = checkio(arrayForIndex)
    newArr = list(dict.fromkeys(arrayForIndex))

    for i in range(0, len(newArr)):
        if countX(arrayForIndex, newArr[i]) == 3:
            consistencies = consistencies + 1

    return consistencies

total = 0
for m in range(0, sessions):
    total = findConsistency(consistencies, m) + total

testFile = open("gymnastics.out", 'w')
testFile.write(str(total))
testFile.close()

