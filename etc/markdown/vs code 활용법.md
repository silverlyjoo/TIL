# vs code 활용법

---------



#### 터미널 사용

- touch 파일명.확장자

  파일 생성

- code 파일명.확장자

  파일 vs code로 열기

> atom 은 atom 파일명.확장자, 서브라임은 sblm 파일명.확장자 이런식



#### 파이썬

- 파일 포맷

  {}.format('one', 'two')

```python
name = '박성주'
e_name = 'Park'

print("안녕하세요 {1} 입니다. My name is {0}".format(name, e_name))
```

- f_string

```python
name = '박성주'
e_name = 'Park'

print(f'안녕하세요.{name}입니다. My name is {e_name}')
```

- 강제 입력

```python
name = "박성주"
print("안녕하세요." + name + "입니다.")
```



#### 로또 자동 5개

```python
for i in range(5):
    numbers = random.sample(range(1,46), 6)
    numbers.sort()
    print(numbers)
```



#### 파이썬 import os 관련 명령어

- os.chdir(r'폴더주소) 

> 작업하고싶은 위치 변경

- os.listdir(폴더주소)

> 위치의 파일 목록

- os.rename(기존이름, 변경할이름)

> 파일 이름 변경



#### 파이썬으로 텍스트 파일 만들기

##### 새로 만들어 열기

```python
f = open("new.txt", "w")
f.write("Hello world!")
f.close()
```

```python
with open("new.txt", "w") as f:
    f.write("Hello !!")
```



##### 텍스트 글씨 추가하기

```python
with open("new.txt", "a") as f:
    f.write("World")
```

##### 텍스트 읽어오기

```python
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()
```

```python
with open("new.txt", "r") as f:
    data = f.read()
    print(data)
```

##### 텍스트에 여러 줄 내용 추가하기

```python
f = open("new.txt", "w")
for i in range(1, 5):
    data = f'{i}번째 줄입니다. \n'
    f.write(data)
f.close()
```

```python
with open("new.txt", "w") as f:
    for i in range(1, 11):
        data = f'{i}번째 줄입니다. \n'
        f.write(data)
```

##### 인코딩하기!!

```python
with open("new.txt", "w", encoding='utf-8') as f:
```

##### 텍스트 직접 bash 에서 읽기

> cat 텍스트파일

##### 탭으로 구분

> \t

##### 한줄넘기기

> \n

##### 텍스트 내용 리턴하기

> readline() : 한줄로 읽어서 리턴
>
> readlines() : 파일 전체를 읽어 list 형태로 리턴

##### 텍스트 좌우 스트립해서 리턴하기

> strip() 활용
>
> line.strip()

