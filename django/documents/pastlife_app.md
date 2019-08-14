## 나의 전생 직업 APP

> 190221 Thu

|        |     이름      |
| :----: | :-----------: |
|  APP   |     jobs      |
| Column | name, pastjob |
| Model  |      Job      |

| 컬럼명  |       데이터 타입        |
| :-----: | :----------------------: |
|  name   | CharField(max_length=20) |
| pastjob | CharField(max_length=30) |

---

## Python `Faker` package

> https://faker.readthedocs.io/en/stable/
>
> https://github.com/joke2k/faker

```bash
$ pip install faker
```

```python
# faker 사용법
from faker import Faker
faker = Faker('ko_kr')
faker.job()
```

```bash
$ python manage.py startapp jobs
```
```python
# settings.py
INSTALLED_APPS = [
    'jobs.apps.JobsConfig',
    ...,
]
```

```python
# jobs/models.py
from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    pastjob = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
```

```bash
$ python manage.py makemigrations jobs 
$ python manage.py migrate jobs  
```

```bash
사용자로부터 이름을 받아
db 에서 이름을 검색해서
1. 있으면 저장된 직업을 가져오기
2. 없으면 faker 로 직업을 새로 만들고 저장해서 가져오기
```

```python
# jobs/views.py
# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
```

```python
# crud/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('boards/', include('boards.urls')),
    path('admin/', admin.site.urls),
]
```

```python
# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
```

```django
<!-- jobs/index.html -->
<body>
    <h1>전생app</h1>
    <p>전생을 알려 드립니다!</p>
    
    <form action="/jobs/pastlife/">
        <input type="text" name="name"/>
        <input type="submit" value="Submit"/>
    </form>
</body>
```

```python
# views.py
from django.shortcuts import render
from faker import Faker
from .models import Job

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    # db 에 이름 있는지 확인
    person = Job.objects.filter(name=name).first()
    # 왼쪽은 DB 컬럼, 오른쪽은 index 에서 넘겨 받아 저장한 name
    # person = Job.objects.get(name=name) # 위에 것보다 이게 더 간단하다. 
    # 하지만 get은 에러메시지를 띄운다. 그래서 우리는 위에껄 사용한다.
    
    # 있으면, 원래 직업 꺼내오고
    if person:  # 만약 person이 있다면 (레코드가 있으면 None이 아니니까 True일 것이다)
        pastjob = person.pastjob
        # person 안에는 person 데이터 객체가 들어가있다. 즉, person안에 들어가있는 pastjob을 가져온다.
    	# 없으면 새로 만들어서 보여주기
    else:
        faker = Faker('ko-kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)# 새로운 레코드를 추가한다. (클래스에 인자를 넘긴다.)
        person.save()
    
    return render(request, 'jobs/pastlife.html', {'person': person})
```
```python
# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pastlife/', views.pastlife, name="pastlife"),
    path('', views.index, name="index"),
]
```
```django
<!-- jobs/pastlife.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>{{ person.name }}님의 전생은 {{ person.pastjob }}입니다</h1>
    <a href="/jobs/">뒤로</a>
</body>
</html>
```

```python
# jobs/admin.py
from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pastjob',]

admin.site.register(Job, JobAdmin)
```

---

### GIPHY

https://giphy.com/

- jobs/views.py

```python
import os 
from django.shortcuts import render
from faker import Faker
import requests
from .models import Job

def pastlife(request):
    name = request.GET.get('name')
    person = Job.objects.filter(name=name).first()

    if person:
        pastjob = person.pastjob
    else:
        faker = Faker('ko-kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)
        person.save()
            
             
    # GIPHY
    GIPHY_API = os.getenv('GIPHY_API')
    url = f"http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={job}&limit=1&lang=ko"
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')
    
    return render(request, 'jobs/pastlife.html', {'person': person, 'image': image})
```

- pastlife.html

  ```html
  <body>
      <h1>{{ person.name }}님의 전생은 {{ person.pastjob }}입니다</h1>
      <img src="{{ image }}">
      <a href="/jobs/">뒤로</a>
  </body>
  ```

  