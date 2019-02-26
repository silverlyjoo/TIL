import sys
sys.stdin = open("contact.txt")


def go(s):
    visited = [0]*101
    queue = [s]
    result = []
    while queue:
        print(queue)
        i = queue.pop(0)

        for j in R[i]:
            if not visited[j]:
                visited[j] = 1
                if j in start:
                    queue.append(j)
                else:
                    result.append(j)




T = 10

for tc in range(1, 1+1):
    l, s = map(int, input().split())
    L = list(map(int, input().split()))
    R = [[] for _ in range((100)+1)]
    start = L[::2]
    end = L[1::2]
    result = []
    for i in range(l//2):
        R[start[i]].append(end[i])

    print(R)
    go(s)
    # print(result)

