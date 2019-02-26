import sys
sys.stdin = open("ndgl_input.txt")


def BFS(sp, V, L):
    visited = [0] * (V+1)
    queue = []
    queue.append(sp)
    while queue:
        val = queue.pop(0)
        for i in L[val]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[val] + 1
    return visited

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    L = [[] for i in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        L[a].append(b)
        L[b].append(a)
    S, N = map(int, input().split())
    print(f'#{tc} {BFS(S, V, L)[N]}')

    # print(f'#{tc} {result}')
