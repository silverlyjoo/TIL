import sys
sys.stdin = open('dutsem.txt')

def sem(a, b):
    for i in range(1, len(a)):
        if eval(str(int(a[:i]))+'+'+str(int(a[i:]))) == int(b):
            return str(int(a[:i]))+'+'+str(int(a[i:]))+'='+b

a, b = input().split()
if sem(a,b):
    print(sem(a,b))
else:
    print('NONE')

