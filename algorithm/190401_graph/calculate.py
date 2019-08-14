import sys
sys.stdin = open('calculate.txt')


def calc(num, idx):

    if idx == 0:
        return num+1
    if idx == 1:
        return num-1
    if idx == 2:
        return num*2
    if idx == 3:
        return num-10


def calcs(nums, M):
    if nums == M:
        return 0

    queue = [[nums, 0]]
    visit[nums] = 1

    while queue:

        snum, cnt = queue.pop(0)
        for idx in range(4):
            nnum = calc(snum, idx)
            if nnum > 1000000 or nnum < 1:
                continue
            if nnum == M:
                return cnt+1
            if not visit[nnum]:
                visit[nnum] = 1
                queue.append([nnum, cnt+1])


T = int(input())
for tc in range(1, T+1):
    result = 0
    N, M = map(int, input().split())
    visit = [0 for _ in range(1000002)]
    print('#{} {}'.format(tc, calcs(N, M)))



