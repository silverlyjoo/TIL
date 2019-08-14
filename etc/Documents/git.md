## git

### [git](https://git-scm.com/book/ko/v1/Git%EB%A7%9E%EC%B6%A4-Git-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)

- 사용자 정보 설정

> 메일주소는 반드시 GitHub 계정과 동일해야하고 유저네임도 맞춰주는 것이 좋다.
>
> `--global` 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다. (만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 `--global` 옵션을 빼고 명령을 실행한다.)

```bash
$ git config --global user.name 'example'
$ git config --global user.email "example@gmail.com"
```

- git 명령어 자동 컬러링

```bash
$ git config --global color.ui true
```

- Mac 에서 한글파일명 깨짐 및 commit 오류 문제 해결

```bash
$ git config --global core.precomposeunicode true
$ git config --global core.quotepath false
```

- 정보 설정 확인

```bash
$ git config --global --list
```

- Git repo 를 처음 생성한 경우

```bash
$ git init
$ git remote add origin https://github.com/example
```

- Git repo 를 clone 한 경우

```bash
$ git clone 주소 (폴더이름)
# 이 경우 git init, git remote add origin - 명령어를 하지 않아도 이미 설정되어 있다.
```

- Commit & Push

```bash
$ git status                    # 현재 폴더의 git 상태 확인(필수, 자주 사용)
$ git add .
$ git commit -m "D01 | 190101 AM | Git"
$ git push -u origin master     # 이후에는 git push 만 해도 동작, git clone 한 경우에도 해당
```

### Git & Github 재설정

```bash
# Git 이름, 이메일 재설정
$ git config --global user.name 'example'
$ git config --global user.email 'example@gmail.com'

# GitHub 로그인 정보 초기화
$ git credential reject
protocol=https
host=github.com
```