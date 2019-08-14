import sys
sys.stdin = open('ssibalfrog.txt')


def upperSearch2(s, e, data):
    # data 이상에서 가장 큰 값의 위치 리턴
    sol = -1
    while s <= e:
        m = (s+e)//2
        if arr[m] < data:  # 데이터 이하이면 오른쪽영역 재탐색
            s = m+1
            sol = m
        else:
            e = m-1
    return sol

# main
N = int(input())
arr = []
for _ in range(N):
    i = int(input())
    arr.append(i)

arr.sort()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        start = arr[j] + (arr[j] - arr[i])
        end = arr[j] + (arr[j] - arr[i])*2

        up = upperSearch2(0, N-1, end+1)
        lo = upperSearch2(0, N-1, start)
        cnt += (up-lo)
print(cnt)