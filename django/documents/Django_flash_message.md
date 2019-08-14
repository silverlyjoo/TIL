## Django flash message

- 핵심 코드

```python
# settings.py 에 해당 코드 추가
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```

```python
# views.py
from django.contrib import messages
...

messages.add_message(request, messages.SUCCESS, "삭제 완료! <a href='/movies/'>홈으로</a>")
```

```django
<!-- example.html -->
{% if messages %}
	{% for message in messages %}
		<div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}" role="alert">{{ message|safe }}</div>
	{% endfor %}
{% endif %}
```

> `|safe` : 플래시 메세지에 html 태그를 사용하고 싶을때 사용한다.

---

- views.py

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
    
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    return render(request, 'movies/detail.html', {'movie': movie})
    
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    messages.add_message(request, messages.SUCCESS, "삭제 완료! <a href='/movies/'>홈으로</a>")
    
    # (1)
    # return redirect(index) 
    
    # or
    # (2)
    return render(request, 'movies/detail.html')
```

- index.html

```django
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>INDEX</title>
</head>
<body>
    <!-- (1) detail 에서 redirect 로 왔을 때-->
    {% if messages %}
        {% for message in messages %}
            <div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}" role="alert">{{ message|safe }}</div>
        {% endfor %}
    {% endif %}

    <h1>INDEX</h1>
    <hr>
    {% for movie in movies %}
        <p>TITLE : <a href="/movies/{{ movie.id }}/">{{ movie.title }}</a></p>
        <p>SCORE : {{ movie.score }}</p>
        <hr>
    {% endfor %}
</body>
</html>
```

- detail.html

```django
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Detail</title>
</head>
<body>
    <!-- (2) 현재 페이지를 render 했을 때-->
    {% if messages %}
        {% for message in messages %}
            <div class="alert {% if message.tags %}alert-{{ message.tags }}{% endif %}" role="alert">{{ message|safe }}</div>
        {% endfor %}
    {% endif %}
    
    <h1>Detail</h1>
    <img src="{{ movie.poster_url }}" alt="movie_img" style="width: 300px; height: 100%;">  
    <p>{{ movie.title }}</p>
    <p>{{ movie.audience }}</p>
    <p>{{ movie.genre }}</p>
    <p>{{ movie.score }}</p>
    <p>{{ movie.description }}</p>
    <a href="/movies/">[목록]</a>
    <a href="/movies/{{ movie.pk }}/update/">[수정]</a>
    <a href="/movies/{{ movie.pk }}/delete/">[삭제]</a>
</body>
</html>
```

