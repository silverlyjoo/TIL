import sys
sys.stdin = open("candy.txt")


def wrap(L):
    while len(L) != 1:
        temp = []
        for i in range(2):
            min_num = min(L)
            min_idx = L.index(min_num)
            temp.append(L.pop(min_idx))
        L.append(sum(temp))
        result.append(sum(temp))

N = int(input())
L = list(map(int, input().split()))
result = []
wrap(L)
print(sum(result))

