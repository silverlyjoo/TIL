import sys
sys.stdin = open('spy.txt')


N, data = input().split()

stack = []
nums = '0123456789'
num = ''
for con in data:
    if con in nums:
        num += con
    else:
        if num:
            stack.append(int(num))
            num = ''
            stack.append(con)
        else:
            stack.append(con)
if len(num):
    stack.append(num)

cnt = 0
ns = [[] for _ in range(51)]

for spy in stack:

    if spy == '<':
        cnt += 1
    elif spy == '>':
        cnt -= 1
    else:
        ns[cnt].append(spy)
print(*ns[int(N)])