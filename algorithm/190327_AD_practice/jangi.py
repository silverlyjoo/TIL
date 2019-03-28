import sys
sys.stdin = open('jangi.txt')


def iswall(y, x):
    if y < 0 or y >= 10: return True
    if x < 0 or x >= 9: return True
    return False


def bfs(sy, sx):


    queue = [[sy, sx]]
    pan[sy][sx] = 2
    dx = [-3, -3, -2, 2, 3, 3, 2, -2]
    dy = [-2, 2, 3, 3, 2, -2, -3, -3]

    wall = [[[-1, 0], [-2, -1]], [[-1, 0], [-2, 1]], [[0, 1], [-1, 2]], [[0, 1], [1, 2]], [[1, 0], [2, 1]],
            [[1, 0], [2, -1]], [[0, -1], [1, -2]], [[0, -1], [-1, -2]]]

    while queue:

        y, x = queue.pop(0)

        for idx in range(8):
            ny = y + dy[idx]
            nx = x + dx[idx]

            walls = wall[idx]

            wx1, wy1 = walls[0]
            wx2, wy2 = walls[1]

            if not iswall(ny, nx) and pan[wy1][wx1] != 0 and pan[wy2][wx2] != 0:


                
                queue.append([ny, nx])
                pan[ny][nx] = 2





T = int(input())

for tc in range(T):


    pan = [[0 for _ in range(9)] for _ in range(10)]

    sy, sx = map(int, input().split())

    ky, kx = map(int, input().split())

    pan[ky][kx] = 3

    sy -= 1
    sx -= 1
    ky -= 1
    kx -= 1


