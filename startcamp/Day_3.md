## Day_3

1. 파이썬 문제풀이 (제어문 모음)

2. html/css 기초

3. flask

   - c9 가입 및 환경설정

   - 플라스크 서버 실행

   - 라우팅 설정
   - html 랜더링
   - variable routing
   - menu 랜덤출력

4. github 페이지

   - icon 바꿔보기 (font-awesome)
   - 색감, 이미지 변경 등등

---

## 1. 파이썬 문제풀이 (제어문)

- 아래 코드의 출력 결과를 예상하라

```python
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")
```

```python
# 정답
3
5
# if - else 구문을 만나면 조건에 충족(True)하는 하나의 구역만 실행한다는 사실 유의!
```

- 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오
  - `input()` : 사용자의 입력 값을 받는다.

```python
# A 1
n = int(input('숫자를 입력하세요: '))
for i in range(n):
    print(i+1)
    
    
# A 2
n = int(input('숫자를 입력하세요: '))
for i in range(1,n+1):
    print(i)
```

- 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 

  '투자 경고 종목입니다'를 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라. 

  - `if x in y` : x 가 in 에 포함되어 있는지 판단. (있다면 True) <-> `if x not in y`

```python
# Q
warn_investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트: {warn_investment_list}")
item = input('투자종목이 무엇입니까?: ')

# A 1
if item in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# A 2
if item.lower() in warn_investment_list:
    print("WARNING!")
else:
    print("SAFE")
```

-  다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하시오.

  - 튜플(tuple)
    - 리스트는 `[` 과`]`으로 둘러싸지만 튜플은 `(` 과 `)` 으로 둘러싼다.
    - 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

- ```python
  # Q
  colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
  
  
  # A1
  deleteindex = [0, 4, 5]
  fruit = []
  
  for i in range(0, len(colors)):
      if i not in deleteindex:
          fruit.append(colors[i])
  print(fruit)
  
  
  # A2
  fruit = []
  
  for color in colors:
      if colors.index(color) not in (0, 4, 5):
          fruit.append(color)
  print(fruit)
  
  
  # A4
  fruit = []
  
  for a in colors:
      if a not in colors[0] and a not in colors[4] and a not in colors[5]:
          fruit.append(a)
  print(fruit)
  ```

- **딕셔너리 조작 연습 기초**

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

# ssafy의 semester1의 기간을 출력하세요
print(ssafy["duration"]["semester1"])

# ssafy dictionary 안에 들어 있는 '대전'를 출력하세요
print(ssafy["location"][1])

# daejeon 의 매니저의 이름을 출력하세요.
print(ssafy["classes"]["daejeon"]["manager"])
```

----

## 2. html/css 기초

>  htmlcss 문서 참고

---

## 3. flask

>  가입 환경 및 설정: c9 초기세팅문서 참고

---

### 라우팅 설정

- `hello.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요!!!"

@app.route("/hello")
def hello():
    return "반가워ㅎㅎㅎㅎ"
```

### HTML rendering

> render 할 html 파일들은 **반드시 `templates` 폴더 안에 있어야 한다.**

```python
from flask import Flask
app = Flask(__name__)

...
    
@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하셔요!!!</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1>여러줄 보내기</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
```

- index.html 랜더링

```python
from flask import Flask, render_template

...

@app.route("/html_render")
def html_render():
    return render_template("index.html")
```

### Variable routing

#### 이름 받아서 출력

```python
@app.route("/html_name/<string:name>")
def html_name(name):
    return render_template("hello.html", your_name = name)
```

- `hello.html`

```python
<h1>안녕하세요!, {{ your_name }}</h1>
```

#### 정수 받아서 계산

```python
@app.route("/math/<int:num>")
def math(num):
    result = num**3
    return render_template("math.html", num = num, result = result)
```

- `math.html`

```python
<h1>{{ num }} 의 세제곱 값은</h1>
<h2>{{ result }} 입니다.</h2>
```

#### 저녁 메뉴 랜덤 뽑기

```python
from flask import Flask, render_template
import random
app = Flask(__name__)

...

@app.route("/dinner")
def dinner():
    list = ["초밥", "탕수육", "삼겹살", "돼지국밥"]
    dict = {
        "초밥": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfF9i7jCNsrSQiCYuzla9I8xxy2owFfgPYtiKyJ7mbPNEbLMZp",
        "탕수육": "https://i1.wp.com/starkaraokeuiuc.net/wp-content/uploads/2017/09/K-11.jpg?fit=639%2C409",
        "삼겹살": "https://cdn.shopify.com/s/files/1/1071/7482/products/tip_4d8d7385-041d-4042-9291-b0b3e7a5945c.jpg?v=1481208412",
        "돼지국밥": "https://dispatch.cdnser.be/wp-content/uploads/2018/11/20181121002235_d426e3e2cc9c45b124f83033e2fb0580.jpg"
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("dinner.html", pick=pick, url=url)
```

- `dinner.html`

```python
<h1>오늘의 저녁은 {{ pick }}</h1>
<img src="{{url}}" alt="{{pick}}사진" height="300" width="400">
```

---

### GibHub

[fontawesome](https://fontawesome.com/)

- 손쉽게 예쁘고 다양한 아이콘 넣기
- class 이름으로 간단하게 아이콘 조작