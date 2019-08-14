import sys
sys.stdin = open("torn_input.txt")


def isel(sL):
    for i in sL:
        if len(i) > 2:
            return False
    return True

def tor(L, D):
    if len(L[0]) == 1:
        return L
    stack = []
    for i in L:
        a = (len(i)+1)//2
        stack.append(i[:a])
        stack.append(i[a:])
    if isel(stack):
        return stack
    else:
        return tor(stack, D)

def rsp(RS, D):
    RS2 = tor(RS, D)
    if len(RS2[0]) == 1:
        return RS2
    else:
        stack = []
        for i in RS2:
            if len(i) == 2:
                if i[0][0] == D[i[0][0]]:
                    stack.append(i[1])
                else:
                    stack.append(i[0])
            else:
                stack.append(i[0])

        return rsp([stack], D)





T = int(input())

for N in range(1, T+1):
    E = int(input())
    D = {'1':'2', '2':'3', '3':'1'}
    KL = list(map(str, input().split()))
    L = [[(b,a) for a,b in enumerate(KL)]]
    print(L)
    # print(tor(L, D))

    # print(RS)
    print(rsp(L, D))