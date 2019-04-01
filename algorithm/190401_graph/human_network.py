import sys
sys.stdin = open('human_network.txt')


def changeinfinite():
    for y in range(N):
        for x in range(N):
            if y != x and nodes[y][x] == 0:
                nodes[y][x] = 0xffffffffff


T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    N = data.pop(0)
    nodes = []
    for i in range(N):
        nodes.append(data[:N])
        data = data[N:]
    changeinfinite()

    for mid in range(N):
        for start in range(N):
            if mid != start:
                for end in range(N):
                    if start!= mid != end:
                        way1 = nodes[start][mid] + nodes[mid][end]
                        way2 = nodes[start][end]
                        nodes[start][end] = min(way1, way2)

    print(nodes)

    result = []
    for node in nodes:
        result.append(sum(node))

    print('#{} {}'.format(tc, min(result)))




