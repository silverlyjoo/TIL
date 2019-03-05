import sys
sys.stdin = open('bingo.txt')


def delnum(num):
    for i in range(5):
        for j in range(5):
            if pan[i][j] == num:
                pan[i][j] = 0
                return


def isbingo():
    global result
    for i in range(5):
        if not pan[i][0] and not pan[i][1] and not pan[i][2] and not pan[i][3] and not pan[i][4]:
            return True
        if not pan[0][i] and not pan[1][i] and not pan[2][i] and not pan[3][i] and not pan[4][i]:
            return True
    if not pan[0][0] and not pan[1][1] and not pan[2][2] and not pan[3][3] and not pan[4][4]:
        return True
    if not pan[0][4] and not pan[1][3] and not pan[2][2] and not pan[3][1] and not pan[4][0]:
        return True
    return False


def isbingo2(i,j):
    global result
    for x in range(4, -1, -1):
        for y in range(5):
            if pan[y][x]:
                return
    result = 1

def dobingo():
    global result
    cnt = 0
    for num in nums:
        cnt += 1
        delnum(num)

        isbingo()
        if result:
            return cnt

# 입력받기
pan = [list(map(int, input().split())) for i in range(5)]
nums = []
for innums in range(5):
    nums += map(int, input().split())
result = 0
print(dobingo())