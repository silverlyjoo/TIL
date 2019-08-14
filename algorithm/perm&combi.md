```python
# 기본구조

def 함수(idx, start):
    
    if idx == N: # 원하는결과수
        print('결과')
        return
    for i in range(start, 경우의수): # 순열 : start = 0 / 결과를 뽑을 수 있는 경우의 수 
        # if visit[i]: continue
        # visit[i] = 1
        check[idx] = i
        함수(idx+1, start or start+1)
        # visit[i] = 0

```



### start 값 있으면(이전에 선택한것부터 시작하면) 조합

- start 에서 시작하면 중복조합
- start + 1 에서 시작하면 조합



### start 값 없으면(처음부터 시작하면) 순열

- visit 체크하면 순열
- visit 체크 안하면 중복순열



