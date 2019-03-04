import sys
sys.stdin = open('gtjs.txt')

def findparent(node):
    if node != 0:
        num1parent.append(R[node][2]) if R[node][2] !=0 else None
        findparent(R[node][2])

def findparent2(node):
    global result
    if node in num1parent:
        result = node
        return
    if node != 0:
        findparent2(R[node][2])

def cntree(node):
    global cnt
    if node != 0:
        cnt += 1
        cntree(R[node][0])
        cntree(R[node][1])


T = int(input())

for tc in range(1, T+1):
    V, E, num1, num2 = map(int, input().split())
    L = list(map(int, input().split()))
    R = [[0 for _ in range(3)] for _ in range(V+1)]
    for i in range(0, len(L), 2):
        if R[L[i]][0]:
            R[L[i]][1] = L[i+1]
        else:
            R[L[i]][0] = L[i+1]
        R[L[i+1]][2] = L[i]
    result = 0
    cnt = 0
    num1parent = []
    findparent(num1)
    findparent2(num2)
    cntree(result)
    print('#{}'.format(tc), result, cnt)







    # print(R)