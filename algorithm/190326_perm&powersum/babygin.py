import sys
sys.stdin = open('babygin.txt')

def realbaby(chk):
    if chk[0] == chk[1] == chk[2]: return True
    if chk[0]+2 == chk[1]+1 == chk[2]: return True
    return False


def isbabygin(n, k, cards, chk):
    global result
    if k==0:
        if realbaby(chk):
            result = True
    else:
        for i in range(n):
            cards[i], cards[n-1] = cards[n-1], cards[i]
            chk[k-1] = cards[n-1]
            isbabygin(n-1, k-1, cards, chk)
            cards[i], cards[n - 1] = cards[n - 1], cards[i]


def babygin(cards):
    chk = [0 for _ in range(3)]
    isbabygin(len(cards), 3, cards, chk)


T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    A = []
    B = []
    result = False
    final = 0
    for idx in range(len(data)):
        if not idx%2:
            A.append(data[idx])
            babygin(A)
            if result and not final:
                final = 1
        else:
            B.append(data[idx])
            babygin(B)
            if result and not final:
                final = 2

    print('#{} {}'.format(tc, final))