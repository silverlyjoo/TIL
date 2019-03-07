import sys
sys.stdin = open('doyak.txt')

# N = int(input())
# L = [int(input()) for i in range(N)]
# L.sort()
# cnt = 0
# for first in range(N-2):
#     for second in range(first+1, N-1):
#         print("N", first, second)
#         print('#', L[first], L[second])
#         print(list(range(2*L[second]-L[first], L[second]+2*(L[second]-L[first])+1)), L[second+1:])
#         print('R',set(range(2*L[second]-L[first], L[second]+2*(L[second]-L[first])+1)) & set(L[second+1:]))
#         # print(set(range(2*L[second]-L[first], L[second]+2*(L[second]-L[first])+1)), set(L[second+1:]))
#         if set(range(2*L[second]-L[first], L[second]+2*(L[second]-L[first])+1)) & set(L[second+1:]):
#             cnt += len(set(range(2*L[second]-L[first], L[second]+2*(L[second]-L[first])+1)) & set(L[second+1:]))
# print(cnt)


N = int(input())
L = sorted([int(input()) for i in range(N)])
cnt = 0
for first in range(N):
    for second in range(first+1, N):
        for third in range(second+1, N):
            if (L[second]-L[first]) <= (L[third]-L[second]) <= 2*(L[second]-L[first]):
                print(L[first], L[second], L[third])
                cnt += 1
print(cnt)