import sys
sys.stdin = open('robot.txt')


def howlong(node1, node2):
    return abs(node1[0]-node2[0])+ abs(node1[1] - node2[1])


def perm(idx, sum):
    global result

    if sum > result:
        return

    if idx >= N:
        if sum < result:
            result = sum
        return

    for i in range(N):
        if not chk[i]:
            chk[i] = 1
            perm(idx+1, sum + memo[idx][i])
            chk[i] = 0




T = int(input())

for tc in range(1, T+1):

    N = int(input())

    r_cookies = list(map(int, input().split()))
    r_robots = list(map(int, input().split()))

    cookies = []
    robots = []

    for i in range(N):
        cookies.append([r_cookies[2*i], r_cookies[2*i +1]])
        robots.append([r_robots[2*i], r_robots[2*i +1]])

    memo = [[0 for _ in range(N)] for _ in range(N)]

    for c in range(N):
        for r in range(N):
            memo[c][r] = howlong(cookies[c], robots[r])

    T = [0 for _ in range(N)]
    chk = [0 for _ in range(N)]
    result = float('inf')
    perm(0, 0)
    print(result)



    
    # print(cookies)




