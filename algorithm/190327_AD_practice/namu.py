import sys
sys.stdin = open('namu.txt')


def cut(height):
    sums = 0
    for tree in trees:
        cutted = tree - height
        if cutted > 0:
            sums += cutted
    return sums


def lowerbns():
    start = min(trees)
    end = max(trees)
    sol = 0

    while start <= end:
        mid = (start+end)//2
        tree = cut(mid)

        if tree == M:
            return mid
        if tree < M:
            sol = mid
            end = mid - 1
        if tree > M:
            start = mid + 1
    return (start+end)//2


N, M = map(int, input().split())
trees = list(map(int, input().split()))
print(lowerbns())

