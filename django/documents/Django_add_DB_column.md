## Django_add_DB_column

- created_at, updated_at 을 추가해보자.

  ```python
  # Create your models here.
  class Board(models.Model):
      title = models.CharField(max_length=100)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  ```bash
  $ python manage.py makemigrations
  ```

---

```bash
You are trying to add the field 'created_at' with 'auto_now_add=True' to board without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1

Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

- 기존에 created_at, updated_at 이 없던 rows(record)들 한테 갑자기 column이 생긴 상황인데, 얘네들한테 created_at, updated_at 에 어떤 값을 기본 값으로 넣을 건지 물어보는 것이다.
- `1` 선택하고, 그 다음 python 인터프리터 같은 곳에서는 그냥 enter 만 입력해도 된다. (원래는 넣고자 하는 값을 넣고 enter 입력해야함.)

```bash
$ python manage.py migrate
```