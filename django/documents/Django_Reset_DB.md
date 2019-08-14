## Django_Reset_DB

1. 일반적인 DB 초기화

   - migrations `0001_`, `0002_` 로 시작하는 파일들을 다 지워준다.

   - `db.sqlite3`를 지워준다.

   - 명령어를 다시 입력한다.

     ```bash
     $ python manage.py makemigrations 
     $ python manage.py migrate
     ```

   - 추가로, superuser(admin) 또한 db에 저장되는 거라서 다시 만들어 주어야 한다.

2. DB 에 존재하는 모든 데이터 레코드를 삭제

```bash
$ python manage.py sqlflush
```

3. 특정 App 의 모든 데이터 레코드를 삭제

```bash
$ python manage.py sqlflush <APP_NAME>
```

4. 특정 App 의 모든 테이블을 삭제

```bash
$ python manage.py migrate <APP_NAME> zero
```