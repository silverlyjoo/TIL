import sys

sys.stdin = open('book.txt')


def comb(idx, sums):
    global msum

    if idx >= N:
        if sums >= B and sums < msum:
            msum = sums
        return
    
    if sums > msum:
        return
    
    comb(idx+1, sums + data[idx])
    comb(idx+1, sums)



T = int(input())

for tc in range(1,T+1):
    N, B = map(int, input().split())
    data = [int(input()) for _ in range(N)]
    msum = float('inf')
    comb(0,0)
    print(msum-B)
    
