import sys
sys.stdin = open('tape.txt')






def comb(idx, cnt, dif):
    global result
    if idx >= N:
        return

    if cnt >= N//2:
        diff = abs(total - 2*dif)
        if result > diff:
            result = diff
        return

    chk[idx] = 1
    comb(idx+1, cnt+1, dif-data[idx])
    chk[idx] = 0
    comb(idx+1, cnt, dif)






N = int(input())

data = list(map(int, input().split()))
total = sum(data)
chk = [0 for _ in range(N)]
result = float('inf')

comb(0, 0, total)
print(result)

