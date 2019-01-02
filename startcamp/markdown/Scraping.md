# Scraping



## request

##### 파이썬 외장함수 깔기

```python
pip install requests
```

##### 리퀘스트

```python
import requests

print(requests.get("https://www.naver.com"))
```

##### html 텍스트

```python
print(requests.get("https://www.naver.com").text)
```

##### 리퀘스트 코드

```python
print(requests.get("https://www.naver.com").status_code)
```



### Scraping

```python
import requests
from bs4 import BeautifulSoup

# print(requests.get("https://www.naver.com"))
# print(requests.get("https://www.naver.com").text)
# print(requests.get("https://www.naver.com").status_code)

req = requests.get("https://finance.naver.com/sise/").text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now")

print(kospi.text)
```

