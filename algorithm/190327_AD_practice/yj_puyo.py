import sys
sys.stdin = open('puyo.txt')


# 4연쇄 검사 + 삭제
def dfs(x, y):
    global flag
    # flag = 1
    visited = [[0] * 6 for _ in range(12)]
    count=0
    Q = [(x, y, arr[x][y])]
    q = [(x, y)]    # 찾은애들
    while Q:
        x, y, c= Q.pop(0)

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=12 or ny<0 or ny>=6: continue
            if visited[nx][ny]: continue
            if arr[nx][ny] != c: continue
            Q.append((nx, ny, c))
            count+=1
            q.append((nx, ny))
            visited[nx][ny] = 1
    # 삭제
    if count>3:
        flag = 0
        for i in range(12):
            for j in range(6):
                if visited[i][j]:
                    arr[i][j] = '.'
    if flag==0:
        return 1

# 내리기
def down():
    global flag, cnt, sjcnt
    flag=1
    end=(0,0)
    for j in range(6):  # 열순서
        # 내릴 위치 확인
        for i in range(11, -1, -1): # 밑에서부터 위로
            if arr[i][j]=='.':
                end = (i, j)
                break
        for k in range(11, -1, -1):
            if arr[k][j]=='.': continue
            if k>i:continue

            if i<1: continue

            flag=0
            arr[k][j], arr[end[0]][end[1]] = arr[end[0]][end[1]], arr[k][j]
            i -= 1
            end = (i, j)
    if not flag:
        sjcnt += 1

# main -----------------------------------------------------

T = int(input())
dx = [-1, 1, 0, 0] # 위 아래 좌 우
dy = [0, 0, -1, 1]

for tc in range(T):
    cnt = 0
    arr = [list(input()) for _ in range(12)]
    flag=0
    sj = 0
    sjcnt = 0
    while True:
        # 뿌요 삭제
        for i in range(12):
            for j in range(6):
                if arr[i][j]=='.': continue
                a = dfs(i, j)
        if sj:
            sjcnt += 1
        # 뿌요 내리기
        down()
        if flag == 1:
            break
        cnt+=1
        for i in range(12):
            print(arr[i])
        print('#')


    # print(sjcnt)
    if sjcnt == 1:
        print(sjcnt)
    elif cnt:
        print(sjcnt+1)
    else:
        print(0)
    # for i in range(12):
    #     print(arr[i])