import sys
sys.stdin = open("forth_input.txt")

def cals(L):
    stack = []
    for i in L:
        if i.isdigit():
            stack.append(int(i))
        elif i == '.':
            if len(stack) < 2:
                return stack[0]
            else:
                return 'error'
        else:
            if len(stack) > 1:
                stack.append(str(int(eval(str(stack.pop(-2))+i+str(stack.pop(-1))))))
            else:
                return 'error'

T = int(input())
for N in range(1, T+1):
    L = list(map(str, input().split()))
    print(f'#{N} {cals(L)}')