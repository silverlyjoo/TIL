import sys
sys.stdin = open("babygin.txt")

def babygin():
    global flag
    cnt = 0
    if data[0] == data[1] == data[2]: cnt += 1
    if data[3] == data[4] == data[5]: cnt += 1
    if data[0]+2 == data[1]+1 == data[2]: cnt += 1
    if data[3]+2 == data[4]+1 == data[5]: cnt += 1

    if cnt == 2:
        flag = 1
        return


def perm(n, k):
    if n == k:
        babygin()

    else:
        for i in range(k, n):
            data[i], data[k] = data[k], data[i]
            perm(n, k+1)
            data[i], data[k] = data[k], data[i]


T = int(input())

for tc in range(1, T+1):

    data = list(map(int, input()))
    flag = 0
    perm(len(data), 0)
    if flag:
        print('babygin')
    else:
        print('no-babygin')