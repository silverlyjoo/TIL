import sys
sys.stdin = open('timemoney.txt')

L = [tuple(map(float, input().split())) for _ in range(5)]
L3 = [j-i for i,j in L]
L2 = []

for i in L3:
    if i >=5:
        L2.append(4)
    elif i <= 1:
        L2.append(0)
    else:
        L2.append(i-1)

money = sum(L2)*10000

if sum(L2) >= 15:
    print(int(money*0.95))
elif sum(L2) <= 5:
    print(int(money*1.05))
else:
    print(int(money))

# print(L, L2, L3)