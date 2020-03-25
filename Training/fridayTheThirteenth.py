"""
ID: ishaan.8
LANG: PYTHON3
TASK: friday
"""
input = open("friday.in", 'r')
output = open("friday.out", 'w')

N = int(input.readline().strip())

monthsWith31 = [1, 3, 5, 7, 8, 10, 12]
monthsWith30 = [4, 6, 9, 11]
centuries = [2000, 2100, 2200, 2300]

monday = 0
tuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0

dayCounter = 1

for i in range(1900, 1900+N):
    for j in range(1, 13):
        if j in monthsWith31:
            days = 31
        elif j in monthsWith30:
            days = 30
        elif j == 2:
            if (i % 4 == 0) and (i != 1900) and i not in centuries:
                days = 29
            elif (i in centuries) and (i % 400 == 0):
                days = 29
            else:
                days = 28
        for z in range(1, days+1):
            if z == 13 and dayCounter == 1:
                monday = monday + 1
            if z == 13 and dayCounter == 2:
                tuesday = tuesday + 1
            if z == 13 and dayCounter == 3:
                wednesday = wednesday + 1
            if z == 13 and dayCounter == 4:
                thursday = thursday + 1
            if z == 13 and dayCounter == 5:
                friday = friday + 1
            if z == 13 and dayCounter == 6:
                saturday = saturday + 1
            if z == 13 and dayCounter == 7:
                sunday = sunday + 1
            dayCounter = dayCounter + 1
            if dayCounter == 8:
                dayCounter = 1

output.write(str(saturday) + ' ' + str(sunday) + ' ' + str(monday) + ' ' + str(tuesday) + ' ' + str(wednesday) + ' ' + str(thursday) + ' ' + str(friday) + '\n')
