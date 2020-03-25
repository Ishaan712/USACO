"""
ID: ishaan.8
LANG: PYTHON3
TASK: test
"""
readfile = open('friday.in', 'r')
writefile = open('friday.out', 'w')
x,y = map(int, readfile.readline().split())
sum = x+y
writefile.write (str(sum) + '\n')
writefile.close()