import sys
sys.stdin = open('minimun_length_tree.txt')


def prim(node, V):


    for i in range(V+1):









T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())

    # data = [list(map(int, input().split())) for _ in range(E)]
    # data.sort(key=lambda x:x[2])
    #
    # print(data)


    L = [[0 for _ in range(V+1)] for _ in range(V+1)]




    for line in range(E):
        n1, n2, w = map(int, input().split())

        L[n1][n2] = w
        L[n2][n1] = w

    for y in range(V+1):
        for x in range(V+1):
            if y != x and L[y][x] == 0:
                L[y][x] = 0xfffffffff







    print(L)




