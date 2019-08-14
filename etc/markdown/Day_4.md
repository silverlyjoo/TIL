## Day_4

INDEX

1. 딕셔너리 문제풀이
2. flask
   - lotto 출력
   - form 을 통한 fake naver, google
   - form 을 통한 요청과 응답
   - opgg 전적검색

---

## 1. 딕셔너리 문제풀이

```python
#1. 평균을 구하세요.
scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40
}
# 1-1
total_score = 0
for score in scores.values():
    total_score = total_score + score
    total_score += score

averge_score = total_score / len(scores)
print(averge_score)

# 1-2
total_score = sum(scores.values())
average_score = total_score/len(scores)
```

```python
# 2. 반 평균을 구하시오
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}

total_score = 0
count = 0

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score += indivisual_score
        count += 1

average_score = total_score / count
print(average_score)
```

```python
# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else:
        # 최저 온도가  cold 보다 더 추우면, cold  에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        # 최고 온도가 hot 보다 더 더우면, hot  에 넣고
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1

print(f"{hot_city}, {cold_city}")
```

---

## 2. flask

### 2-1. 로또 출력하기

```python
@app.route("/lotto")
def lotto():
    num_list = list(range(1,46))
    lucky = random.sample(num_list, 6)
    return render_template("lotto.html", lucky=sorted(lucky))
```

- `lotto.html`

```html
<h1>{{ lucky }}</h1>
{% for num in lucky %}
	<h1>{{ num }}</h1>
{% endfor %}
```

### 2-2 fake naver/google

- https://search.naver.com/search.naver?query={검색어}
- https://www.google.com/search?q={검색어}

```python
@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")
```

- `naver.html`

```html
<h1>네이버 검색!!</h1>
<form action="https://search.naver.com/search.naver">
    <input type="text" name="query"/>
    <input type="submit">
</form>
```

- `google.html`

```html
<h1>구글 검색!!</h1>
<form action="https://www.google.com/search">
    <input type="text" name="q"/>
    <input type="submit">
</form>
```

### 2-3 form 을 통한 요청과 응답

- ping 이 `name` 이라는 이름표를 가진 input 값을 pong 으로 보내면(`action="/pong"`)
- pong 은 `name` 이름표를 받아 input 값을 받는다. (`request.args.get('name')`)

```python
@app.route("/ping")
def hell():
    return render_template("ping.html")

@app.route("/pong")
def hi():
    user_name = request.args.get('name')
    # user_name = request.args['name']
    return render_template("pong.html", user_name=user_name)
```

- `ping.html`

```html
<form action="/pong">
    <input type="text" name="name"/>
    <input type="submit" value="submit">
</form>
```

- `pong.html`

```html
<h1>{{ user_name }}</h1>
```

### 2-4 opgg 전적검색

> 첫 조건을 잘 잡는 것이 관건.
>
> 1. 소환사가 존재하는지 존재하지 않는지.
> 2. 존재한다면 랭크전적이 있는지 없는지.

#### 1. 소환사가 있는지 없는지 판단, 있다면 승리 수 알아보기

- `sohwan.html`

```html
<form action="/summoner">
	소환사의 아이디를 입력하세요.
	<input type="text" name="name">
    <input type="submit" value="submit">
</form>
```

```python
@app.route("/sohwan")
def sohwan():
    return render_template('sohwan.html')

@app.route("/summoner")
def summoner():
    name = request.args.get('name')
    req = requests.get(f"http://www.op.gg/summoner/userName={name}").text
    soup = BeautifulSoup(req, "html.parser")
    summoner = soup.select_one("body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    
    if summoner:
        return render_template("opgg.html", name=name, wins=wins.text)
    else:
        return render_template("nouser.html", name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```

- `nouser.html`

```html
<h1>{{ name }} 소환사는 계정이 없습니다.</h1>
```

- `opgg.html`

```html
<h1>{{ name }} 의 이번 시즌 랭크 승: {{ wins }}</h1>
```

#### 2. 계정은 있으나 랭크 전적이 없을때

- `notier.html`

```html
<h1>{{ name }} 소환사는 랭크 전적이 없습니다.</h1>
```

```python
@app.route("/summoner")
def summoner():
    name = request.args.get('name')
    req = requests.get(f"http://www.op.gg/summoner/userName={name}").text
    soup = BeautifulSoup(req, "html.parser")
    summoner = soup.select_one("body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    tier = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierRank > span")
    
    if summoner:
        if tier.text == "Unranked":
            return render_template("notier.html", name=name)
        else:
            return render_template("opgg.html", name=name, wins=wins.text)
    else:
        return render_template("nouser.html", name=name)
    
if __name__ == "__main__":
app.run(host="0.0.0.0", port=8080, debug=True)
```

#### 3. flash / redirect / url_for

> `redirect()` 를 활용하면, 사용자의 조회 위치를 변경할 수 있다.
>
> `url_for()` 는 route 주소로 이동하는 것이 아닌 정의된 **함수**를 호출한다. 
>
> `flasing messages` 은 기본적으로 요청의 끝에 메시지를 기록하고 그 다음 요청에서만 그 메시지에 접근할 수 있게 한다. [doc](http://flask.pocoo.org/docs/1.0/patterns/flashing/)

- `sowhan.html`

```html
<h3>
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
    {% endif %} 
{% endwith %}
</h3>
<form action="/summoner">
	소환사의 아이디를 입력하세요.
	<input type="text" name="name">
    <input type="submit" value="submit">
</form>
```

```python
from flask import Flask, render_template, request, url_for, redirect, flash

...

@app.route("/sohwan")
def sohwan():
    return render_template("sohwan.html")
    
@app.route("/summoner")
def summoner():
    name = request.args.get('name')
    url = f"http://www.op.gg/summoner/userName={name}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, "html.parser")
    summoner = soup.select_one("body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    tier = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div > span")
    
    if summoner and tier.text == "Unranked":
        flash(f"{name} 소환사는 랭크 전적이 없습니다.")
        return redirect(url_for('sohwan'))
    elif summoner:
        return render_template("opgg.html", name=name, wins=wins.text)
    else:
        flash(f"{name} 소환사가 없습니다.")
        return redirect(url_for('sohwan'))

if __name__ == "__main__":
    app.secret_key = "Super_secret_key"			
    app.run(host="0.0.0.0", port=8080, debug=True)
```
