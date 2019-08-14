import sys
sys.stdin = open('dojagi.txt')


def combs2(idx, cnt, start):
    if cnt >= M:
        print(chk2)
        return

    if idx >= N:
        return


    chk2[idx] = 1
    combs(idx + 1, cnt+1, start)
    chk2[idx] = 0
    combs(idx + 1, cnt, start)


def combs(idx, cnt, start):
    global result
    if cnt >= M:
        re = sorted(chk)
        if re not in result:
            result.append(re[:])
        return

    if idx >= N:
        return
    
    for i in range(start, N):
        chk[idx] = matterial[i]
        combs(idx+1, cnt+1, i+1)



T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    matterial = list(map(int, input().split()))
    chk2 = [0 for _ in range(N)]
    chk = [0 for _ in range(M)]
    result = []

    # combs2(0, 0, 0)
    combs(0, 0, 0)
    print(len(result))

