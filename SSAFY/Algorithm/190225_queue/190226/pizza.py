import sys
sys.stdin = open("pizza_input.txt")

def iszero():
    for i in range(len(L)):
        if L[i][0] == 0:
            return str(i)
    return False


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [[val,idx] for idx, val in enumerate(list(map(int, input().split())))]
    out = []
    while len(out) < M:
        # print(L)
        while not iszero():
            print('굽기전',L)
            if len(L) > N:
                H = N
            else:
                H = len(L)
            bake = L[:H]
            L = L[H:]
            # print(bake)
            for i in bake:
                i[0] //= 2
            L = bake + L
            print('구은후',L)
            print()
        out.append(L[int(iszero())][1])
        L.pop(int(iszero()))


    print('out', out)
    print()
