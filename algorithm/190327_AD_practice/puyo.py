import sys
sys.stdin = open('puyo.txt')



def iswall(y, x):
    if y < 0 or y >= 12: return True
    if x < 0 or x >= 6: return True
    if field[y][x] == '.': return True
    return False


def visit():
    r_visited = [[0 for _ in range(6)] for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if field[y][x] != '.':
                r_visited[y][x] = 1
    return r_visited


def isvisit(visited):
    for y in range(12):
        for x in range(6):
            if visited[y][x] ==1:
                return True
    return False


def findstart(visited):
    for y in range(12):
        for x in range(6):
            if visited[y][x] == 1:
                return (y, x)


def isfour(start, visited):

    sy, sx = start
    que = [[sy, sx]]
    V = [[sy, sx]]

    cnt = 1

    while que:

        y, x = que.pop(0)
        color = field[y][x]

        for i in range(4):

            ny, nx = y + dy[i], x + dx[i]

            if iswall(ny, nx): continue
            if [ny, nx] in V: continue

            if field[ny][nx] == color:
                que.append([ny, nx])
                V.append([ny, nx])
                cnt += 1



    if cnt >= 4:
        for items in V:
            y, x = items
            visited[y][x] = 0
        return V
    else:
        for items in V:
            y, x = items
            visited[y][x] = 2

def delpuyo(L):

    dels = L[:]

    for i in dels:
        y, x = i
        field[y][x] = '.'


def array(visited):

    for x in range(6):
        idx = 11
        change = 11


        while idx >= 0:
            if visited[idx][x] != 0 and visited[change][x] != 0:
                change -= 1
                idx -= 1
                continue
            if visited[idx][x] == 0:
                idx -= 1
            else:
                if visited[change][x] == 0:
                    visited[change][x] = visited[idx][x]
                    field[change][x] = field[idx][x]
                    visited[idx][x] = 0
                    field[idx][x] = '.'
                    idx -= 1
                    change -= 1
                else:
                    change -= 1


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T+1):
    field = [list(input()) for _ in range(12)]
    cnt = 0
    flag = 1
    while flag:
        flag = 0
        visited = visit()
        while isvisit(visited):
            start = findstart(visited)
            V = isfour(start, visited)
            if V:
                delpuyo(V)
                flag = 1
        if flag:
            cnt += 1
        array(visited)
    print(cnt)



