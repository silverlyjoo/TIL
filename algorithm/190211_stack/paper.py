import sys
sys.stdin = open("paper_input.txt")

def paper(n):
    L = [1, 3]
    if n > 1:
        for i in range(2, n):
            L.append(2*L[i-2] + L[i-1])
    return L[n-1]

T = int(input())
for N in range(T):
    y = int(input())
    print(f'#{N+1} {paper(y//10)}')