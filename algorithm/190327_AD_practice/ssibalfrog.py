import sys
sys.stdin = open('ssibalfrog.txt')


def lowerSearch(start, end, data):

    sol = -1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] >= data : # 데이터 이상이면 왼쪽 재탐색
            sol = mid
            end = mid - 1
        else:
            start = mid + 1 # 오른쪽 탐색
    return sol

def upperSearch(start, end, data):

    sol = -1
    while start <= end:
        mid = (start + end) // 2
        if L[mid] <= data:
            sol = mid
            start = mid + 1
        else:
            end = mid -1
    return sol

N = int(input())
L = []
for _ in range(N):
    L.append(int(input()))
L.sort()
cnt = 0

for first in range(len(L)-2):
    for second in range(first+1, len(L)-1):
        range1 = L[second] + (L[second] - L[first])
        range2 = L[second] + (L[second] - L[first]) * 2

        lo = lowerSearch(second+1, N-1, range1)
        if lo == -1 or L[lo] > range2: continue
        up = upperSearch(second+1, N-1, range2)
        cnt += (up-lo+1)

print(cnt)
