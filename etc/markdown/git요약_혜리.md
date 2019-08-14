# git

 : 분산 버전관리 시스템(DVCS : *Distributed Version Control System*)

- 기반 서비스 : `Github`, ` Bitbucket` 개인 프로젝트 관리하기 좋음,  `gitlab`  협업하기 좋음

- 차이가 무엇이고 수정 이유를 log로 남길 수 있다.

- 작업 흐름

  - **add** 		커밋할 목록에 추가
  - **commit** 	커밋(create a snapshot) 만들기
  - **push**		현재까지의 역사 (commits)가 기록되어 있는 곳에 

- **git 기본**

  ```bash
  student@DESKTOP MINGW64 /
  $ git --version
  git version 2.20.1.windows.1
  
  student@DESKTOP MINGW64 /
  $ git config --global user.name "sshyeri"
  
  student@DESKTOP MINGW64 /
  $ git config --global user.email "sshyeri.k@gmail.com"
  
  student@DESKTOP MINGW64 /
  $ git config --global --list
  user.name=sshyeri
  user.email=sshyeri.k@gmail.com
  
  ```

- **git에 파일 업로드**

```bash
student@DESKTOP MINGW64 ~/desktop
$ cd til
student@DESKTOP MINGW64 ~/desktop/til (master)
$ ls
1217_2.md  markdown_pract.md
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git add markdown_pract.md
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git add 1217_2.md
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git commit -m "first commit"
[master (root-commit) db4623a] first commit
 2 files changed, 200 insertions(+)
 create mode 100644 1217_2.md
 create mode 100644 markdown_pract.md
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git log
commit db4623a8045f13e888a31bf0d8068191d28bf649 (HEAD -> master)
Author: sshyeri <sshyeri.k@gmail.com>
Date:   Mon Dec 17 17:41:38 2018 +0900
    first commit
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git remote add origin https://github.com/sshyeri/TIL.git
student@DESKTOP MINGW64 ~/desktop/til (master)
$ git push -u origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 2.02 KiB | 2.02 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To https://github.com/sshyeri/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
student@DESKTOP MINGW64 ~/desktop/til (master)
$
```
두번째 커밋 시에는 $ git remote add origin https://github.com/sshyeri/TIL.git 불필요, git push만 써도 됌

add 여러개 가능, commit에 여러개 쌓고 한번에 푸시 가능

commit은 버전 달아주는 것 ! 도장 찍는 듯이.