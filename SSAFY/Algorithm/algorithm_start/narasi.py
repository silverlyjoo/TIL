import sys
sys.stdin = open("narasi_input.txt")
T = 10
for times in range(T):
    N = int(input())
    narasi = list(map(int, input().split()))
    count = 0
    for time in range(N+1):
        high_point = 0, 0
        low_point = 100, 0
        for idx in range(len(narasi)):
            if narasi[idx] > high_point[0]:
                high_point = narasi[idx], idx
            if narasi[idx] < low_point[0]:
                low_point = narasi[idx], idx
        if time >= N:
            break
        narasi[high_point[1]] -= 1
        narasi[low_point[1]] += 1
        if high_point[0] - low_point[0] == 0:
            break
    print(f'#{times+1} {high_point[0]-low_point[0]}')


# import sys
# sys.stdin = open("inputs/flatten_input.txt")
# def find_min(counts):
#     for idx, c in enumerate(counts):
#         if c != 0:
#             return idx
#
# def find_max(counts):
#     for idx, c in enumerate(counts[::-1]):
#         if c != 0:
#             return len(counts) - idx - 1
# def dump(count, n, m, temp):
#     count[n] -= temp
#     count[m] -= temp
#     count[n + 1] += temp
#     count[m - 1] += temp
#
# def solution(dump_num, boxes):
#     count = [0] * 101
#     for i in boxes:
#         count[i] += 1
#     n = find_min(count)
#     m = find_max(count)
#     while dump_num > 0:
#         if count[n] > count[m]:
#             temp = count[m]
#             if dump_num - temp < 0:
#                 temp = dump_num
#             dump(count, n, m, temp)
#             dump_num -= temp
#             m -= 1
#         elif count[n] < count[m]:
#             temp = count[n]
#             if dump_num - temp < 0:
#                 temp = dump_num
#             dump_num -= temp
#             dump(count, n, m, temp)
#             n += 1
#         else:
#             temp = count[n]
#             if dump_num - temp < 0:
#                 temp = dump_num
#             dump(count, n, m, temp)
#             dump_num -= temp
#             m -= 1
#             n += 1
#     return find_max(count) - find_min(count)
#
# def main():
#     for test_case in range(10):
#         dump_num = int(input())
#         boxes = list(map(int, input().split()))
#         print(f"#{test_case + 1} {solution(dump_num, boxes)}")
#
# if __name__ == '__main__':
#     main()