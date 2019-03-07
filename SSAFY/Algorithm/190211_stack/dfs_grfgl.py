import sys
sys.stdin = open('grpgl_input.txt')


def go(node, G):
    global result

    if node == G:
        result = 1
    else:
        if not visit[node]:
            visit[node] = 1
            for i in L[node]:
                go(i, G)





T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    visit = [0]*(V+1)
    result = 0
    L = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        L[s].append(e)
    S, G = map(int, input().split())

    go(S,G)
    print(f'#{tc} {result}')