import sys
sys.stdin = open('pukit.txt')


def comb(idx, cnt, ssum, bsum):
    global result

    if idx >= N:
        # if cnt!=0:
        if ssum != 1 and bsum != 0:
            a = abs(bsum-ssum)
            if a <= result:
                result = a
        return
    
    comb(idx+1, cnt+1, ssum*data[idx][0], bsum+data[idx][1])
    comb(idx+1, cnt, ssum, bsum)


N = int(input())
data = []
for _ in range(N):
    s, b = map(int, input().split())
    data.append((s,b))

result = float('inf')
comb(0,0,1,0)
print(result)
