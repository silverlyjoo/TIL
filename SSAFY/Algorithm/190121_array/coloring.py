
import sys
sys.stdin = open("coloring_input.txt")
from pprint import pprint


T = int(input())
for case in range(T):
    N = int(input())
    count = 0
    template = [[0 for i in range(10)] for i in range(10)]
    for color_case in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for rcolor in range(r1,r2+1):
            for ccolor in range(c1,c2+1):
                template[rcolor][ccolor] += color
                if template[rcolor][ccolor] == 3:
                    count += 1
    pprint(template)
    print(f'#{case+1} {count}')







