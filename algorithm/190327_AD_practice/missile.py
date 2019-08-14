import sys
sys.stdin = open('missile.txt')


def isrange(node1, node2):
    length = abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])
    if prange >= length: return True
    return False


def islive():
    cnt = 0
    for i in ships:
        if i[2]>0:
            cnt += 1
    return cnt


def perms(idx):
    global shipN, misN, result

    if idx >= misN:
        lives = islive()
        if result > lives:
            result = lives
        return


    for i in range(shipN):

        if ships[i][2] > 0:

            ship1 = [ships[i][0], ships[i][1]]
            inrange = []

            for j in range(shipN):
                ship2 = [ships[j][0], ships[j][1]]

                if isrange(ship1, ship2):
                    inrange.append(j)

            for k in inrange:
                ships[k][2] -= power

            perms(idx+1)

            for k in inrange:
                ships[k][2] += power




shipN = int(input())

ships = []

for i in range(shipN):
    x, y, e = map(int, input().split())
    ships.append([y, x, e])

misN, power, prange = map(int, input().split())
result = float('inf')

perms(0)
print(result)







