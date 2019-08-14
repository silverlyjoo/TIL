import sys
sys.stdin = open("pizza_input.txt")

def melt():
    v = bake.pop(0)
    v[0] //= 2
    if v[0] == 0:
        result.append(v[1])
        if L:
            bake.append(L.pop(0))
    else:
        bake.append(v)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = [[val,idx] for idx, val in enumerate(list(map(int, input().split())))]
    bake = [L.pop(0) for _ in range(N)]
    result = []
    while len(result) < M:
        melt()
    print('#{} {}'.format(tc, result[-1]+1))