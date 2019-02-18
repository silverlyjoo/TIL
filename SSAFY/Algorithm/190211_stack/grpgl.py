import sys
sys.stdin = open("grpgl_input.txt")


def goto(S, G, L):
    global result
    for i in L[S]:
        if i == G:
            return 1
        else:
            goto(i, G, L)


T = int(input())
for N in range(T):
    V, E = map(int, input().split())
    L = [[] for _ in range(V+1)]
    result = 0
    for C in range(E):
        a, b = map(int, input().split())
        L[a].append(b)
    S, G = map(int, input().split())
    print(f'#{N+1} {goto(S, G, L)}')
    # print(S, G)
    # print(L)
    # print(result)