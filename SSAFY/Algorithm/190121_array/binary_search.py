import sys
sys.stdin = open("binary_search_input.txt")


def binary_search(start, end, page):
    count = 0
    while start <= end:
        count += 1
        test = int((start + end) / 2)
        if test == page:
            return count
        elif page < test:
            end = test
        else:
            start = test
    return None

T = int(input())
for case in range(T):
    P, A, B = map(int, input().split())
    result = ""
    if (binary_search(1, P, A)) < (binary_search(1, P, B)):
        result = "A"
    elif (binary_search(1, P, A)) == (binary_search(1, P, B)):
        result = "0"
    else:
        result = "B"
    print(f'#{case+1} {result}')


