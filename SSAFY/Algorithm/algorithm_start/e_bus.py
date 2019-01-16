# import sys
# sys.stdin = open("e_bus_input.txt")

# T = int(input())

# for i in range(T):
#     dist, length, cj_num = map(int, input().split())
#     cj_points = list(map(int, input().split()))
#     cj_point = dist
#     count = 0
#     re_count = dist
#     while cj_point < length:
#         if cj_point in cj_points:
#             cj_point += dist
#             count += 1
#             re_count = dist
#         else:
#             cj_point -= 1
#             re_count -= 1
#         if re_count == 0:
#             count = 0
#             break
#     print(f'#{i+1} {count})


import sys
sys.stdin = open("inputs/bus_input.txt")
def solution(K, N, stops):
    answer = prev = 0
    status = K
    for i in range(len(stops) - 1):
        status -= stops[i] - prev
        if status < 0:
            return 0
        if stops[i + 1] - stops[i] > status:
            status = K
            answer += 1

        prev = stops[i]
    last = stops[-1]
    status -= last - prev
    if N - last > K:
        return 0
    elif N - last > status:
        answer += 1
    return answer

def main():
    T = int(input())
    for test_case in range(T):
        K, N, M = map(int, input().split())
        stops = list(map(int, input().split()))
        print(f"#{test_case + 1} {solution(K, N, stops)}")

if __name__ == '__main__':
    main()









import sys
sys.stdin = open("inputs/bus_input.txt")
def solution(K, N, stops):
    """
    :param K: 한번 충전시 갈 수 있는 정류장 수
    :param N: 종점까지 정류장 갯수
    :param stops: 충전기가 설치된 정류장 목록 (번호로 주어짐)
    :return: 최소한의 충전 횟수

    SW Expert Academy 4831. 전기 버스(d3) / 시간복잡도 : O(n) 예상
    """
    answer = prev = 0
    # answer는 최종 정답, prev는 현재 정거장과 다음 정거장의 거리를 계산하기 위해 사용
    status = K
    # status는 현재 충전 현황을 뜻함
    for i in range(len(stops) - 1):
        status -= stops[i] - prev
        # 그 다음 충전기가 있는 정류장까지 갔으므로 충전 현황을 계산
        if status < 0:
            return 0 # 만약 0보다 작다면 충전량으로 현재 정류소까지 갈 수 없으므로 0 반환
        if stops[i + 1] - stops[i] > status:
            status = K
            answer += 1
        """
        핵심로직!
        우리의 관심사는 충전소가 있는 정류장마다 충전하는 것이 아니다!
        충전 횟수를 최소화해야하므로 그다음 현재 가지고 있는 충전량으로 그다음 충전소까지
        갈 수 있는지 계산하여 충전하도록 만듦
        """
        prev = stops[i] # 이전 정류소 갱신
    # for문에서 마지막 정류소를 계산하지 않았으므로 마지막 정류소까지 계산
    last = stops[-1]
    status -= last - prev
    if N - last > K:
        return 0
    elif N - last > status:
        answer += 1
    return answer

def main():
    T = int(input())
    for test_case in range(T):
        K, N, M = map(int, input().split())
        stops = list(map(int, input().split()))
        print(f"#{test_case + 1} {solution(K, N, stops)}")

if __name__ == '__main__':
    main()

