# 190221 Homework

##### 1. Django에서는 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹 사이트에 요청하게 하는 공격을 막는 기능을 기본적으로 동작시킨다. 위의 공격은 무엇을 의미하는가?

```
CSRF
```



##### 2. 기본적으로 Django에서 views.py에 함수들을 정의할 때 request인자 값을 넣어주어야 한다. request를 활용해서 아래의 폼을 통해서 들어온 데이터를 가져오는 코드를 작성하세요.

```python
title = request.POST.get('title')
```



##### 3. 다음은 사용자가 이미 작성한 글을 수정하기 위해서 기존의 글을 보여주는 edit 페이지를 위한 views.py의 코드이다.

```python
def edit(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'board/edit.html', {'post': post})
```

##### 아래의 코드에 기존의 데이터를 보여줄 수 있도록 코드를 수정하세요.

```html
<form action="/posts/{{ post.id }}/update/" method="POST">
    {% csrf_token %}
    <input type="text" name="title" id="title" value="{{ post.title }}">
    <input type="text" name="content" id="content" value="{{ post.content }}">
    <input type="submit" name="submit">
</form>
```