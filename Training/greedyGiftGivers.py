"""
ID: ishaan.8
LANG: PYTHON3
TASK: gift1
"""
input = open('friday.in', 'r')
output = open("friday.out", 'w')
numOfPeople = int(input.readline().strip())

people = []
dictOfPeople = {}

for i in range(numOfPeople):
    name = input.readline().strip()
    dictOfPeople[name] = 0
    people.append(name)

calculating = True

while calculating:
    money = 0
    remainder = 0
    personGiving = input.readline().strip()
    if not personGiving:
        break
    amount, namOfReceivers = map(int, input.readline().split())
    dictOfPeople[personGiving] = dictOfPeople[personGiving] + (amount*-1)
    if namOfReceivers == 0:
        money = 0
    elif amount % namOfReceivers == 0:
        money = amount / namOfReceivers
        remainder = 0
    else:
        remainder = amount % namOfReceivers
        money = int(round((amount-remainder)/namOfReceivers))
    dictOfPeople[personGiving] = dictOfPeople[personGiving] + remainder
    for i in range(namOfReceivers):
        receiver = input.readline().strip()
        dictOfPeople[receiver] = dictOfPeople[receiver] + money

for i in people:
    output.write(i + " " + str(round(dictOfPeople[i])) + "\n")