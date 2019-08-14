import sys
sys.stdin = open("gl.txt")

T = input()

stack = []
result = 0
for i in T:

    if not stack:
        stack.append(i)
        result += 10
    elif stack[-1] == i:
        result += 5
        stack.append(i)
    else:
        result += 10
        stack.append(i)
print(result)
