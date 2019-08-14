import sys
sys.stdin = open("container.txt")


T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    weights = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    weights.reverse()
    trucks.reverse()

    sums = 0

    for truck in trucks:

        for idx in range(len(weights)):
            if truck >= weights[idx]:
                sums += weights[idx]
                weights.pop(idx)
                break

    print('#{} {}'.format(tc, sums))




