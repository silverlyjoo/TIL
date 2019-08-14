import sys
sys.stdin = open("candy.txt")


def wrap(L):
    global result
    while len(L) != 1:
        L.sort(reverse=True)
        a = L.pop()+L.pop()
        L.append(a)
        result += a

N = int(input())
L = list(map(int, input().split()))
result = 0
wrap(L)
print(result)