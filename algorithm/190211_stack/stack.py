# SIZE = 100
# stack = [0]* SIZE
# top = -1
#
# def push(item):
#     global top
#     if top > SIZE -1:
#         return
#     else:
#         top += 1
#         stack[top] = item

# def pop():
#     global top
#     if top == -1:
#         print("stack is Enpty!")
#         return 0;
#     else:
#         result = stack[top]

# def push(item):
#     s.append(item)
#
# def pop():
#     if len(s) == 0:
#         return False
#     else:
#         return s.pop()

s = []

sampletext = ""

def isgood(text):
    L = []
    for ele in text:
        if ele == '(':
            L.append(ele)
        elif ele == ')':
            if len(L) == 0:
                return False
            L.pop()
    if L:
        return False
    else:
        return True

print(isgood('()()((()))'))
print(isgood('((()((((()()((()())((())))))'))



