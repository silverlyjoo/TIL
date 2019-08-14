import sys
sys.stdin = open("text_del_input.txt")

def couple(Text):
    for i in range(len(Text)-1):
        if Text[i] == Text[i+1]:
            return couple(Text[:i]+Text[i+2:])
    return len(Text)

T = int(input())

for N in range(T):
    Text = input()
    print(f'#{N+1} {couple(Text)}')