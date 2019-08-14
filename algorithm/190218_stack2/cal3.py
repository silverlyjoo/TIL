import sys
sys.stdin = open("cal3_input.txt")

def cals(T):
    result = []
    stack = []
    D = {'*':3, '/':3, '+':2, '-':2, '(':1}
    for i in T:
        # 닫는괄호일때
        if i == ')':
            while True:
                if stack[-1] != '(':
                    result.append(stack.pop())
                else:
                    stack.pop()
                    break
        # 피연산자일때
        elif i not in D:
            result.append(i)

        # 연산자 또는 여는괄호 일때
        else:
            if i == '(':
                stack.append(i)
            elif stack:
                while stack:
                    if D[stack[-1]] < D[i]:
                        stack.append(i)
                        break
                    else:
                        result.append(stack.pop())
            else:
                stack.append(i)
    while stack:
        result.append(stack.pop())
    return result

def cals2(L):
    stack = []
    for i in L:
        if i.isdigit():
            stack.append(int(i))
        else:
            if len(stack) > 1:
                stack.append(str(int(eval(str(stack.pop(-2))+i+str(stack.pop(-1))))))
            else:
                return 'error'
    return stack[0]


T = 10
for N in range(1, T+1):
    G = int(input())
    S = input()
    print(cals2(cals(S)))
