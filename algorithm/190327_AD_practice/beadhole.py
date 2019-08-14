import sys
sys.stdin = open('beadhole.txt')


def iswall(y, x):
    if pan[y][x] == '#': return True
    return False


def hole(bsy, bsx, rsy, rsx, hy, hx):
    global cnt

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    redq = [[rsy, rsx, 1]]
    blueq = [[bsy, bsx, 1]]

    while redq:
        ry, rx, rc = redq.pop(0)
        by, bx, bc = blueq.pop(0)

        for i in range(4):

            nry = ry + dy[i]
            nrx = rx + dx[i]
            nby = by + dy[i]
            nbx = bx + dx[i]

            if iswall(nry, nrx) and iswall(nby, nbx): continue
            if iswall(nry, nrx):
                nry = ry
                nrx = rx
            if iswall(nby, nbx):
                nby = by
                nbx = bx
            if [nby, nbx, nry, nrx] in visit: continue
            if rc == 11 or bc == 11: continue
            if nry == nby and nrx == nbx: continue
            if nby == hy and nbx == hx: continue
            if nry == hy and nrx == hx:
                cnt = rc
                return
            redq.append([nry, nrx, rc + 1])
            blueq.append([nby, nbx, rc + 1])
            visit.append([nby, nbx, nry, nrx])
    else:
        cnt = -1


T = int(input())
for tc in range(1, T+1):
    Y, X = map(int, input().split())
    pan = [list(input()) for _ in range(Y)]

    for y in range(Y):
        for x in range(X):
            if pan[y][x] == 'B':
                bsy, bsx = y, x
            if pan[y][x] == 'R':
                rsy, rsx = y, x
            if pan[y][x] == 'H':
                hy, hx = y, x
    cnt = 0
    visit = [[bsy, bsx, rsy, rsx]]
    hole(bsy, bsx, rsy, rsx, hy, hx)
    print(cnt)
