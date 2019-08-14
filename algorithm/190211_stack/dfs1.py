from pprint import pprint
import sys
sys.stdin = open("input_dfs1.txt")

N = int(input())
inputlist = list(map(int, input().split()))

G = [[0 for _ in range(N)] for _ in range(N)]
visited = [0 for _ in range(N)]

for i in range(0, len(inputlist), 2):
    G[inputlist[i]][inputlist[i+1]] = 1
    G[inputlist[i+1]][inputlist[i]] = 1

def DFS_REcursive(G, N, v):
    visited[v] = 1
    print(v, end=" ")
    for i in range(1, N):
        if not visited[i] and G[v][i]:
            DFS_REcursive(G, N, i)

DFS_REcursive(G, 8, 1)
# print(result)



