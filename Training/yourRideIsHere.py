"""
ID: ishaan.8
LANG: PYTHON3
TASK: ride
"""
readfile = open('ride.in','r')
writefile = open('ride.out', 'w')
comet = readfile.readline().strip()
group = readfile.readline().strip()

total = 1
for i in comet:
    total = total * (ord(i)- 64)

modComet = total % 47

total1 = 1
for i in group:
    total1 = total1 * (ord(i) - 64)

modGroup = total1 % 47

if int(modComet) == int(modGroup):
    writefile.write("GO" + '\n')
else:
    writefile.write("STAY" + '\n')

writefile.close()