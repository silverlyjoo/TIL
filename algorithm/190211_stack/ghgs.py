import sys
sys.stdin = open("ghgs_input.txt")

def isgh(T):
    L = []
    for i in T:
        if i == '(' or i == '{':
            L.append(i)
        elif i == ')':
            if not L:
                return 0
            else:
                if L[-1] != '(':
                    return 0
                else:
                    L.pop()
        elif i == '}':
            if not L:
                return 0
            else:
                if L[-1] != '{':
                    return 0
                else:
                    L.pop()
    if L:
        return 0
    else:
        return 1

C = int(input())

for N in range(C):
    T = str(input())
    print(f'#{N+1} {isgh(T)}')

