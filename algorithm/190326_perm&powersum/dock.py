import sys
sys.stdin = open('dock.txt')


def Work(truck):
    global cnt
    start, end = truck
    for work in range(start, end):
        if visited[work]:
            return
    for work in range(start, end):
        visited[work] = 1
    cnt += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    visited = [0 for _ in range(25)]

    cnt = 0

    data =[]
    for _ in range(N):
        st, ed = map(int, input().split())

        data.append([st, ed])


    data.sort(key=lambda x:x[1])

    for truck in data:
        Work(truck)
    print('#{} {}'.format(tc, cnt))
