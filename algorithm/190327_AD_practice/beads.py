
a = [1,2,3]
b = [0,0,0]
chk = [0,0,0]
N = 3

def DFS(no):
    if no >= N:
        print(*b)
        return

    for i in range(N):
        if chk[i]: continue
        chk[i] = 1
        b[no] = a[i]
        DFS(no+1)
        chk[i] = 0

DFS(0)