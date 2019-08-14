

def queen(idx):
    global cnt
    if idx >= N:
        cnt += 1
        return

    for i in range(N):
        if chk1[i]: continue
        if chk2[idx + i]: continue
        if chk3[(N-1) - (idx-i)]: continue

        chk1[i] = chk2[idx + i] = chk3[(N-1) - (idx-i)] = 1
        queen(idx+1)



N = int(input())

data = [[0 for _ in range(N)] for _ in range(N)]
chk1 = [0 for _ in range(N)]
chk2 = [0 for _ in range(2*N+1)]
chk3 = [0 for _ in range(2*N+1)]
P = [0 for _ in range(N)]
cnt = 0
queen(0)
print(cnt)
