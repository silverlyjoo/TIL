import sys
sys.stdin = open("num_card_input.txt")

T = int(input())
for i in range(T):
    N = int(input())
    cards = str(input())
    num_list = [0]*10
    for k in cards:
        num_list[int(k)] += 1
    max_card = (0, 0)
    for j in range(len(num_list)):
        if num_list[j] >= max_card[1]:
            max_card = (j, num_list[j])
    print(f'#{i+1} {max_card[0]} {max_card[1]}')