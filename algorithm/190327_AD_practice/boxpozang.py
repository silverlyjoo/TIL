import sys
sys.stdin = open('boxpozang.txt')


def comb(idx, asum, bsum, pasta, pastb):
    global result


    if idx >= N:
        sums = asum + bsum
        if result < sums:
            result = sums
        return

    if boxes[idx] < pasta:
        comb(idx+1, asum + boxes[idx], bsum, boxes[idx], pastb)
    if boxes[idx] > pastb:
        comb(idx + 1, asum, bsum + boxes[idx], pasta, boxes[idx])
    comb(idx + 1, asum, bsum, pasta, pastb)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    result = 0
    comb(0, 0, 0, 1000, 0)
    print(result)

