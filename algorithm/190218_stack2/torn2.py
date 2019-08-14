import sys
sys.stdin = open("torn_input.txt")

def tor(L,D):
    # print(L)
    if len(L) > 2:
        stack1 = []
        stack2 = []
        a = (len(L)+1) // 2
        stack1 += L[:a]
        stack2 += L[a:]
        return tor([tor(stack1, D),tor(stack2, D)], D)
    elif len(L) == 2:
        if L[1][0] == D[L[0][0]]:
            return L[1]
        else:
            return L[0]
    else:
        return L[0]

T = int(input())
for N in range(1, T+1):
    E = int(input())
    D = {'1':'2', '2':'3', '3':'1'}
    KL = list(map(str, input().split()))
    L = [(b,a) for a,b in enumerate(KL)]
    result = tor(L,D)[1]+1
    # print(L)
    # print(tor(L,D))
    print(f'#{N} {result}')