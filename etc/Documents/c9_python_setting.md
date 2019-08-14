## c9 파이썬 환경설정

- package 업데이트

```bash
$ sudo apt-get update
```

---

### [pyenv](https://github.com/pyenv/pyenv)

- 설치

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

- 환경변수 설정

```bash
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

$ source ~/.bashrc
# 또는 exec "$SHELL"
```

- python 설치
> ubuntu openssl 이슈 때문에, python 3.6.7을 설치해야 함.

```bash
$ pyenv install --list		# 설치할 수 있는 목록 확인
$ pyenv install 3.6.7
$ pyenv global 3.6.7
$ pyenv rehash
$ python -V
$ pyenv versions
```

---

### [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv#pyenv-virtualenv)

> 추후 장고에서 사용할 예정입니다.

- 설치

```BASH
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

- 환경변수 설정

```bash
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ source ~/.bashrc
```

- 가상환경 만들기

```bash
$ pyenv virtualenv <파이썬버전> <가상환경 이름> # (1) 특정 파이썬 버전으로 가상환경 생성

$ pyenv virtualenv <가상환경이름>  # (2) 그냥 현재 파이썬 버전으로 생성하고 싶다면

$ pyenv versions				   # pyenv 를 이용해 만든 파이썬 버전들을 출력

$ pyenv virtualenvs				   # 설치된 가상환경 목록만 확인
```

- 가상환경 사용하기 - 1 (global)

```bash
# 가상환경 활성화
$ pyenv activate <가상환경 이름>
# 활성화되면 커맨드라인 앞에 가상환경 이름이 나옴.
# 예시) (test37) yourid:~/workspace/ $

# 가상환경 비활성화
$ pyenv deactivate
```

- **가상환경 사용하기 - 2 (local)**

> local 은 해당 디렉토리를 빠져나오면 자동으로 deactivate 된다.

```bash
### [주의] 설정 전 가상환경으로 지정 할 디텍토리로 이동 !!!

# 현재 디렉토리를 특정 가상환경으로 설정
$ pyenv local <가상환경 이름>

# 디렉토리 가상환경 설정 취소 (가상환경 폴더에서 숨김파일 삭제)
$ rm -rf .python-version
```

- 가상환경 삭제

```bash
# 가상환경 삭제
$ pyenv uninstall <가상환경 이름>
```

---

## [pip](https://pip.pypa.io/en/stable/installing/)

- 설치 + 업그레이드

```bash
$ pip install -U pip
```

- 설치된 파이썬 패키지 목록

```bash
$ pip list
```

---

### [flask](http://flask.pocoo.org/)

> 파일 이름은 자유지만 `flask.py` 는 사용해선 안되며 **`app.py` 를 사용하는 것이 기본적인 원칙**이다.
>
> 파일 이름이 app.py 가 아닐경우 (예를들어 `project.py` 인 경우) 아래 처럼 실행한다.
>
> ```bash
> $ export FLASK_APP=project.py 		# 한번만하면 더이상 하지 않아도 됨
> $ flask run 						# 서버 실행 (local 기준)
> ```

- 설치

```bash
$ pip install flask
```

- 서버 실행 (c9 기준)

```bash
$ flask run --host=0.0.0.0 --port=8080
$ flask run --host 0.0.0.0 --port 8080
$ flask run --host=$HOST --port=$PORT
$ flask run -h $IP -p $PORT
```

- 편하게 서버 실행

```python
import os
```

```python
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

```bash
$ python app.py
```