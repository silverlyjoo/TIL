# Django_README

장고 전반적인 내용 중 views.py 를 기본 CRUD 과정으로 요약했습니다

모든 view 함수들은 CRUD 로 설명 가능하니 편하게 암기하고 60점을 넘깁시다.

화이팅

[TOC]

#### 절대암기수칙

```
1. 모든 form 은 is_valid() 해야한다.
2. login 시에는 AuthenticationForm, password 변경시에는 PasswordChangeForm
3. user 모델 사용시에는 get_user_model(), 로그인시 사용시에는 form.get_user()
4. Password 변경은 메소드 사용법이 조금씩 다르므로 주의해서 암기
```


## Create

#### 1. 기본 create

##### 필요한 개념

`login_required`

GET

```python
form = Form() # form 양식전달 페이지 렌더
```

POST

```python
form = Form(request.POST) # POST 요청 양식에 넣음
post = form.save(commit=False) # 유저 정보 받기 위해 잠시 대기
post.user = request.user # 유저 입력
post.save() # is_valid() > save
```

> 유저정보 저장 전 commit=False!!



#### 2. Signup

##### 사전체크

```python
if request.user.is_authenticated: # 괄호없음, 로그인 되있을 시 리턴
    return redirect
```

GET

```python
form = UserCustomCreationForm() # form 양식 페이지 렌더
```

POST

```python
form = Form(request.POST) # POST 요청 양식에 넣음
user = form.save() # is_valid() > save
auth_login(request, user) # 로그인 해주고 리다이렉트
```



#### 3. Login

##### 사전체크

```python
if request.user.is_authenticated: # 괄호없음, 로그인 되있을 시 리턴
    return redirect
```

GET

```python
form = AuthenticationForm() # form 양식 페이지 렌더
```

POST

```python
form = Form(request, request.POST) # POST 요청 양식에 넣음
auth_login(request, form.get_user()) # form 에서 유저 정보 추출해서 로그인 후 리다이렉트
```

> 로그인의 경우 Django 에서 만들어준 폼을 세션으로 보내야 하기 때문에 db에 저장하는 것과 메소드 사용할때 인자를 넣는 부분에서 약간 차이가 있지만 기본적인 create 와 구조가 동일하니 편하게 공부합시다.



#### 4. N: Create

종속 모델 create 에서 추가되는점

```python
comment.post_id = post_pk
# .save(commit=False) 이후 유저 등록과 함께 글 위치도 등록시킨 후 .save()
```



## Update

#### 1. 기본 Update

`login_required`

```python
post = get_object_or_404() # 원래 대상 가져오기
if request.user != post.user: # 작성자와 접근자가 다르면 리턴
    return redirect
```

GET

```python
form = Form(instance=post) # 대상을 양식에 넣어서 페이지 렌더
```

POST

```python
form = Form(request.POST, instance=post)
# instance 를 넣는 이유 : 새롭게 생성되는게 아닌 원래 값에 덮어쓰도록 하기위해
form.save() # is_valid() > save
```



#### 2. 회원정보 Update

`login_required`

GET

```python
form = UserCustomChangeForm(instance=request.user) # 유저정보를 양식에 넣어서 페이지 렌더
```

POST

```python
form = Form(request.POST, instance=request.user) # instance 자리에 현재 유저정보를넣음
form.save() # is_valid() > save
```

> create 때와 마찬가지. 회원정보 업데이트도 기본 업데이트와 큰 차이없으므로 편히 공부하자

#### 3. Password Change

GET

```python
pwd_chg_form = PasswordChangeForm(request.user) # 유저정보 넣어주고 렌더, instance 가아님
```

POST

```python
pwd_chg_form = PasswordChangeForm(request.user, request.POST)
# 암기 팁: 비밀번호는 중요하니까 유저정보도 받은 후 post 요청을 받는다고 생각하고 넣자
user = pwd_chg_form.save() # is_valid() > save 후 로그인 업데이트를 위해 변수에 저장
update_session_auth_hash(request, user) # request 데이터와 바뀐 비밀번호를 세션에 업데이트
```



## Delete

#### 1. 기본 Delete

`login_required`

`require_POST`

```python
post = get_object_or_404() # 대상 가져오기
if request.user != post.user: # 작성자와 접근자가 다르면 리턴
    return redirect
post.delete()
```

#### 2. Logout

```python
auth_logout(request) # 이 이상 무엇이 필요한가.
```

#### 3. 회원정보 Delete

`login_required`

`require_POST`

```python
request.user.delete() # 이 이상 무엇이 필요한가.
```



## Like, Follow

`login_required`

```python
post = get_object_or_404() # 좋아할 대상 가져오기
user = request.user
if post.like_users.filter(pk=user.pk).exists(): # .exists() : QuerySet 전용 함수, filter 뒤
    post.like_users.remove(user)
else:
    post.like_users.add(user)

# in 으로 탐색해도 됨
if request.user in post.like_users.all():
	post.like_users.remove(request.user)
else:
	post.like_users.add(request.user)
```





## 기타

#### Template 에서 사용되는 method 정리

- request.resolver_match.url_name == 'create'

  > 현재 html 에 접근한 url_name 확인



- post.like_users.count

  post.like_users.all | length

  > 쿼리셋안에 객체 수 반환



- user.is_athenticated

  > 로그인 확인




#### views.py import 목록

```python
# posts

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_http_methods, require_POST

# accounts

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
```

