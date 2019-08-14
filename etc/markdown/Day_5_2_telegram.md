## Day_5_2_telegram

### Telegram Chatbot

### 1. 텔레그램 설치

- Telegram 가입 및 로그인
- <https://telegram.org/>
- 데스크탑 앱 or 웹 버전 사용 권장 (폰에서도 알림 받아볼 수 있도록 로그인 해놓기)
- 전화번호 인증 통해서 가입을 해야 이용 가능

---

### 2. 봇 생성

- `@Botfather` 검색

- `시작` 버튼 클릭

- `/newbot` 입력

- 봇 이름 생성 (중복 가능)

- username 생성

  > 중복되지 않는 유니크한 이름 & bot 으로 끝나는 이름

- `token`, `url` 주소 얻기

  > **API Token**은 비밀번호 같은 것 / 절대 노출되지 않도록 관리
  >
  > **보안 설정을 하지 않고 github 에 공유하지 않도록 주의 또 주의한다.**

- url 클릭하여 봇 활성화 후 시작 버튼 클릭

- [텔레그램 봇 api](https://core.telegram.org/bots)

---

### 3. 챗봇 만들기

- **requests** 모듈 [[doc]](http://docs.python-requests.org/en/master/)

  - requests.get(url) 함수를 사용하면 해당 웹페이지 호출 결과를 가진 `Response 객체`를 리턴한다.

    > Response 객체는 HTML Response 와 관련된 여러 attribute들을 가지고 있는데, 예를 들어, Response의 status_code 속성을 체크하여 HTTP Status 결과를 체크할 수 있고, Response 에서 리턴된 데이터를 문자열로 리턴하는 text 속성 등이 있다.

- requests 체험해보기

```python
import requests

url = 'https://api.github.com/'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.text)
print(response.json())
```

#### 3.1 chat_id 가져오기

- 나에게 메세지를 보내려면, telegram에서 지정한 내 고유 `chat id` 값을 알아야 함.
- 우리는 bot 의 관리자이니 해당 bot 으로 누군가가 message 를 보내면, 그 사람의 chat_id 를 알아낼 수 있음. 그래야 bot 이 그 사람에게 메세지를 보내줄수 있다.
- 텔레그램 클라이언트에서 내가 생성한 bot 을 이름으로 검색해서 찾은 다음 start 버튼을 누르고 (그러면 `start` 라는 메세지가 전송 됨.
- `getUpdates` 는 bot 이 받은 모든 메세지를 확인 가능한 정해진 `method` 들 중 하나. 

```python
import requests

token = ""
method_name = "getUpdates"
url = f'https://api.telegram.org/bot{token}/{method_name}'

print(url)
print(requests.get(url))
```

#### 3.2 나에게 메세지 보내기

```python
import requests

token = ""
method_name = "getUpdates"
url = f'https://api.telegram.org/bot{token}/{method_name}'


chat_id = 
method_name = "sendmessage"
msg = "안녕하세요ㅎㅎ"
msg_url = f'https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}'

print(msg_url)
print(requests.get(msg_url))
```

#### 3.3 chat_id 를 json 에서 가져오기

```python
import requests

token = ""
method_name = "getUpdates"
url = f'https://api.telegram.org/bot{token}/{method_name}'
update = requests.get(url).json()

chat_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"
msg = "안녕하세요ㅎㅎ"
msg_url = f'https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}'

print(msg_url)
print(requests.get(msg_url))
```

#### 3.4 token 보안설정 - 환경변수 세팅

- `.bash_profile`

```bash
# [주의] export 이후로는 공백이 없어야한다.
export TELEGRAM_BOT_TOKEN='...'
```

```bash
$ source ~/.bash_profile
```

```python
import requests
import os

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f'https://api.telegram.org/bot{token}/{method_name}'
update = requests.get(url).json()

chat_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"
msg = "안녕하세요ㅎㅎ"
msg_url = f'https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}'

print(msg_url)
print(requests.get(msg_url))
```

#### 3.5 코스피 정보 가져오기

- Beautiful Soup library 설치 [[doc]](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

```bash
$ pip install bs4
```

- Beautiful Soup 체험해보기

```python
from bs4 import BeautifulSoup
url = 'https://www.google.co.kr/'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
```

- **코스피 가져오기**

```python
import requests
from bs4 import BeautifulSoup
import os

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f'https://api.telegram.org/bot{token}/{method_name}'
update = requests.get(url).json()


chat_id = update["result"][0]["message"]["from"]["id"]
method_name = "sendmessage"

url_cos = "https://finance.naver.com/sise/"
html_cos = requests.get(url_cos).text
soup = BeautifulSoup(html_cos, 'html.parser')
select = soup.select_one('#KOSPI_now') 
msg = "코스피: " + select.text
msg_url = f'https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}'

print(msg_url)
print(requests.get(msg_url))
```

---

### 3. Heroku 배포하기

#### 3-1. scheduler 활용을 위한 배포시

> flask 서버를 돌리는 것이 아닌 상황
> 카드 등록 필요 (무료이지만 scheduler 활용하려면 카드 등록이 필요함)

1) `runtime.txt` 파일 루트에 만들기

```bash
$ echo "python-3.6.7" >> runtime.txt
```

2) `requirements.txt` 파일 루트에 만들기

```bash
$ pip freeze > requirements.txt
```
>  혹시 있으면 삭제 해야할 것. heroku에서 안됨. pyenv 안했으면 있을 수도.
>
> - pygobject
> - python-apt
> - python-editor
> - unattended-upgrades

3) commit 

```powershell
$ git init
$ git add . 
$ git commit -m "heroku setting"
```

4) heroku 배포 

> `프로젝트명` 은 heroku 에 이미 있는 프로젝트명은 설정이 불가하니까 unique 하게 해야한다.
>
> 예를 들면 juno_telegram_bot.
>
> 프로젝트명을 주지 않으면 랜덤 값으로 이름이 정해짐.

```powershell
$ heroku login
$ heroku create 프로젝트명
$ git push heroku master
#  build 성공 확인
```

**settings > config Vars에서  환경변수 설정 ** 

- Settings 탭의 Config Vars 에서 key, value 설정.

![image-20181221001901887](./img/1.png)

![image-20181221001946586](./img/2.png)

![image-20181221002026754](./img/3.png)

---

#### 3-2. flask와 함께 배포하기

> DB 없을때 가정, 아래 두개 하고 맨 위로 올라가면 됨. cron job 등록 대신에 명령

1) gunicorn 설치 및 설정- heroku 서버 

(1) gunicorn 설정

```powershell
$ pip install gunicorn
```

(2) 루트에 Procfile 생성(**확장자 없음**)
```
web: gunicorn app:app
```

(4) 서버 실행 테스트
```
$ gunicorn app:app
```

---

### 4. 챗봇 삭제하기

1. BotFather 에게 `/deletebot` 입력
2. 삭제할 봇 선택
3. `Yes, I am totally sure.` 입력

---

### 주의사항

**1. requests 한글 깨짐 문제** [[doc]](http://pythonstudy.xyz/python/article/403-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Web-Scraping)

- Response 객체의 text 속성은 str 클래스 타입으로서 보통 requests 모듈에서 자동으로 데이타를 인코딩해 준다. 만약 인코딩 방식을 변경해야 한다면, text 속성을 읽기 전에 Response의 encoding 속성을 변경하면 된다.
- 인코딩이 유니코드 인코딩(예: `utf-8` 등)이거나 한글 인코딩(예: `euc-kr`)이면 일반적으로 한글이 깨지지 않지만, `ISO-8859-1`와 같이 영문 인코딩이면 한글이 깨지게 된다.

```python
>>> import requests
>>> url = requests.get('http://finance.naver.com') 
>>> url.encoding
'euc-kr'
```

- 해결책
  - 미리 Response 객체의 encoding 을 한글인코딩(예: `euc-kr`)이나 `None` (인코딩 추측을 하지 않도록) 으로 지정한 후, text 속성을 읽어서 확인해보면 된다.

```python
import requests
 
url = requests.get('###')
url.encoding = None   		# 1. None 
# url.encoding = 'euc-kr'  	# 2. 한글 인코딩
 
html = url.text
print(html)
```