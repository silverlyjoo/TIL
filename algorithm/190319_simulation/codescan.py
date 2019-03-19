import sys
sys.stdin = open('codescan.txt')


codes = [
    '112',
    '122',
    '221',
    '114',
    '231',
    '132',
    '411',
    '213',
    '312',
    '211'
]


def iswall(y, x, N, M):
    if y<0 or y>=N: return True
    if x<0 or x>=M: return True
    return False


# def putcode(N, M):
#     result = []
#     for y in range(1, N+1):
#         for x in range(4*(M)-1, -1, -1):
#             if data2[y][x] == '1' and data2[y-1][x] == '0':
#                 flag = 1
#                 pattern = []
#                 ny, nx = y, x
#                 cnt = 0
#
#                 while not iswall(ny, nx, N+1, 4*M):
#                     if data2[ny][nx] == str(flag) and data2[ny-1][nx] == '0':
#                         cnt += 1
#                         nx -= 1
#                     elif data2[ny][nx] != str(flag) and data2[ny-1][nx] == '0' and data2[ny-1][nx-1] == '0' and data2[ny-1][nx+1] =='0':
#                         pattern.append(cnt)
#                         cnt = 1
#                         nx -= 1
#                         flag = (flag + 1)%2
#                     else:
#                         cnt = 1
#                         nx -= 1
#                         flag = 1
#                 result.append(pattern)
#                 break
#
#     return result



def putcode(N, M):
    result = []
    for y in range(1, N+1):
        ny, nx = y, 4*M-1
        if data2[ny][nx] == '1' and data2[ny-1][nx] == '0':
            flag = 1
            pattern = []
            cnt = 0
            while not iswall(ny, nx, N+1, 4*M) and len(pattern) != 8:
                if data2[ny][nx] == str(flag) and data2[ny-1][nx] == '0':
                    cnt += 1
                    nx -= 1
                elif data2[ny][nx] != str(flag) and data2[ny-1][nx] == '0':
                    pattern.append(cnt)
                    cnt = 1
                    nx -= 1
                    flag = (flag + 1)%2
                else:
                    cnt = 1
                    nx -= 1
                    flag = 1
            result.append(pattern)
        else:
            nx -= 1

    return result


T = int(input())

for tc in range(1, T+1):
    # print('##', tc)
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    data2 = ['' for _ in range(N)]

    for i in range(N):
        for j in data[i]:
            a = bin(int(j, 16))[2:]
            dif = 4-len(a)
            data2[i] += '0'*dif+a

    data2.insert(0, '0'*4*M)

    L = putcode(N, M)



    answer = []



    while L:
        i = L.pop(0)
        # print('#',len(i))
        if len(i) <= 32:
            K = i[:]
            RE = ''.join(map(lambda x:str(x//min(K)), K))
            code = []
            for j in range(8):
                pat = RE[:3]
                RE = RE[4:]
                code.append(codes.index(pat))
            code.reverse()
            verify = 0
            for i in range(0, 8, 2):
                verify += code[i]*3 + code[i+1]
            if not verify%10:
                answer.append(sum(code))

        else:
            L.append(i[-31:])
            L.append(i[:-32])

    print(sum(answer))