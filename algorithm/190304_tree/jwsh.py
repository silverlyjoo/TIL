import sys
sys.stdin = open('jwsh.txt')



def inorder(node, result):
    if node != 0:
        inorder(fc[node], result)
        result.append(content[node])
        inorder(sc[node], result)




T = 10

for tc in range(1, T+1):
    N = int(input())
    idx = [0] * (N + 1)
    fc = [0] * (N + 1)
    sc = [0] * (N + 1)
    content = [0] * (N + 1)
    result = []
    for i in range(N):
        temp = list(input().split())
        sidx = int(temp[0])
        scontent = temp[1]
        content[sidx] = scontent
        if sidx * 2 <= N:
            fc[sidx] = int(temp[2])
            if sidx *2 + 1 <= N:
                sc[sidx] = int(temp[3])

    inorder(1, result)
    print('#{}'.format(tc),''.join(result))