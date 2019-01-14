# 알고리즘?



#### IM 을 따자

> 다중 for 문

#### AD 를 따자

> 완전검색 (경우의수따지기 - 재귀함수 필요)
>
> `DP` 활용 - Dynamic Program (동적 계획법)

#### PRO를 따자

> 메인 함수와 매개변수를 주고 함수를 구현하라.
>
> `알고리즘`보다는 `코딩 숙련도`가 중요



#### 사이트 추천

https://swexpertacademy.com/



#### C의 역사

>  Algol > B > C 로 이어지는 언어
>
> `데니스 리치` 가 `unix` 운영체제 구축을 위해 만듬



#### JAVA의 역사

> `Sun`에서 만들어서 `Oracle`로 넘어감
>
> OAK > JAVA 이름 바뀜. 자바산 커피를 즐겨 마심.
>
> 객체 지향의 시작
>
> 범용언어. 
>
> 안드로이드는 자바로만듬.
>
> (아이폰은 object-C로 만들었대)



#### C# 의 시작

> `Microsoft` 에서 만듬
>
>  JAVA 의 장점과 C++ 의 장점을 가져옴



## 알고리즘의 정의

> 유한한 단계를 통해 문제를 해결하기 위한 절차나 방법



- 알고리즘 공부할땐 연필로 쓰면서 공부해라



### 시간복잡도 비교

- P (Polynomial time)

> 다항식 시간(polynomial-time)의 알고리즘으로 풀리는 decision problem의 집합

O(logn) 이진탐색

O(n) 순차탐색

O(nlogn) Quick, Merge, heap

O(n^2) 선택, 버블, 삽입

O(n^3) 모든쌍 최단경로

--------

- NP   (polynomial-time nondeterministic)

>   비결정적 다항식시간(polynomial-time nondeterministic) 알고리즘으로 풀리는 decision problem의 집합

O(2^n) 부분집합

O(n!) TSP(traveling salesman problem)





`Gravity` 문제

```python
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
maxHeight = 0

for i in range(len(data)):
	maxHeight = len(data) - (i+1)   # i행의 최대 낙차 값(그 이후 모든 행 검사)
	for j in range(i+1, len(data), 1)   # 2번째 행과 비교
		if data[i] <= data[j]:   # 아래 행이 i행보다 상자가 많으면 최대낙차값을 1감소
			maxHeight -= 1
	if result < maxHeight:
		result = maxHeight
print(result)
```





## 완전검색 (Exaustive Search)

> 모든 경우의수를 나열해보고 확인하는 기법



모든 경우의 수를 생성하고 테스트하기때문에 수행 속도는 느리지만 해답을 찾아내지 못할 확률이 낮다.



`{1, 2, 3}으로 순열만들기`

```python
for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```



## 탐욕 [Greedy] 알고리즘





## 정렬의 종류

#### 버블정렬



#### 카운팅정렬



#### 선택정렬



#### 퀵정렬



#### 삽입정렬



#### 병합정렬



