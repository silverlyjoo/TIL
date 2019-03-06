import sys
sys.stdin = open('chocolate.txt')

def one(l, h):
    # l 중복
    for i in l:
        if l.count(i) > 1:
            return False
    
    for j in h:
        if h.count(j) > 1:
            return False
    return True

def two(l, h):
    cnt = 0
    for i in l:
        if i in h:
            cnt += 1
    
    if cnt > 2:
        return False
    else:
        return True


N = int(input())
L = []
H = []
for _ in range(N):
    l, h = input().split()
    L.append(l)
    H.append(h)

result = 0
for tc in range(N):
    l, h = L[tc], H[tc]
    if not one(l, h) or not two(l, h):
        result += 1

print(result)
