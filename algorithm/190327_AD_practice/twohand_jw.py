import sys
sys.stdin = open('twohand_jw.txt')



def ganueng(idx, left, right, target):
    global flag
    if idx >= choo:
        if left + target == right:
            flag = True
        return

    ganueng(idx + 1, left + choos[idx], right, target)
    ganueng(idx + 1, left, right + choos[idx], target)
    ganueng(idx + 1, left, right, target)


choo = int(input())
choos = list(map(int, input().split()))
bead = int(input())
beads = list(map(int, input().split()))

for i in beads:
    flag = False
    ganueng(0, 0, 0, i)
    if flag:
        print('Y', end=' ')
    else:
        print('N', end=' ')
