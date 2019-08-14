import sys
sys.stdin = open("sjg.txt")





T = int(input())
L = [input().strip() for _ in range(T)]
L2 = L[:]
L2 = list(map(int, L2))

max_h = 0
max_idx = 0

for i in range(len(L)):
    while len(L[i]) > 1:
        stack = []
        for j in L[i]:
            stack.append(int(j))
        L[i] = str(sum(stack))


L = list(map(int, L))


for i in range(len(L)):
    if L[i] > max_h:
        max_h = L[i]
        max_idx = i
    elif L[i] == max_h:
        if L2[max_idx] > L2[i]:
            max_h = L[i]
            max_idx = i

print(L2[max_idx])