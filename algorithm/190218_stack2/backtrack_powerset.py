def process_solution(a, k):
    for i in range(1, k+1):
        if a[i] : print(data[i], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k)

    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3]
a = [0] * NMAX
backtrack(a, 0, 3)

# 백트레킹_가지치기
def process_solution(a, k, ans):
    if ans != 10:
        return
    global cnt

    for i in range(1, k+1):
        if a[i]:
            print(data[i], end=" ")
    cnt += 1
    print()


def make_candidates(a, k, input_number, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input_number, ans):
    if ans > 10 : return
    global MAXCANDIDATES, total_cnt
    c=[0]*MAXCANDIDATES

    if k == input_number:
        process_solution(a, k, ans)
    else:
        k += 1
        ncands = make_candidates(a,k, input_number, c)
        for i in range(ncands):
            a[k] = c[i]
            if a[k]:
                backtrack(a, k, input_number, ans + data[k])
            else:
                backtrack(a, k, input_number, ans)
    total_cnt += 1

cnt = 0
total_cnt = 0
MAXCANDIDATES = 100
NMAX = 100
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [0]*NMAX
ans = 0
backtrack(a, 0, 10, 0)


print(f'count: {cnt}')
print((f'total_count: {total_cnt}'))