import sys
sys.stdin = open('jangi.txt')


def iswall(y, x):
    if y < 0 or y >= 10: return True
    if x < 0 or x >= 9: return True
    return False


def bfs(sy, sx):


    queue = [[sy, sx, 0]]
    pan[sy][sx] = 2
    dx = [-3, -3, -2, 2, 3, 3, 2, -2]
    dy = [-2, 2, 3, 3, 2, -2, -3, -3]

    wall = [[[-1, 0], [-2, -1]], [[-1, 0], [-2, 1]], [[0, 1], [-1, 2]], [[0, 1], [1, 2]], [[1, 0], [2, 1]],
            [[1, 0], [2, -1]], [[0, -1], [1, -2]], [[0, -1], [-1, -2]]]

    while queue:

        y, x, turn = queue.pop(0)
        for idx in range(8):
            ny = y + dy[idx]
            nx = x + dx[idx]

            walls = wall[idx]

            wx1, wy1 = x + walls[0][0], y + walls[0][1]
            wx2, wy2 = x + walls[1][0], y + walls[1][1]
            
            if not iswall(ny, nx) and pan[wy1][wx1] != 3 and pan[wy2][wx2] != 3:
                if pan[ny][nx] == 3:
                    return turn + 1
                if pan[ny][nx] == 0:
                    queue.append([ny, nx, turn + 1])
                    pan[ny][nx] = 2
    else:
        return -1

pan = [[0 for _ in range(9)] for _ in range(10)]
sy, sx = map(int, input().split())
ky, kx = map(int, input().split())
pan[ky][kx] = 3
print(bfs(sy, sx))


