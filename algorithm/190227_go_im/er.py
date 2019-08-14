import sys
sys.stdin = open("er.txt")


A = 300
B = 60
C = 10

a = 0
b = 0
c = 0

T = int(input())
namugi = T

if T >= A:
    a = T//A
    T %= A
    namugi %= A
if T >= B:
    b = T//B
    T %= B
    namugi %= B
if T >= C:
    c = T//C
    T %= C
    namugi %= C

if not namugi:
    print(a, b, c)
else:
    print(-1)
