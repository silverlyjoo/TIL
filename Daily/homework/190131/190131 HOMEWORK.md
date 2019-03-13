# 190131 HOMEWORK

### SQLite RDBMS



#### 아래 동작을 수행하기 위한 SQL 을 각각 작성하세요.



##### 다음과 같은 스키마를 가지는 DB 테이블 friends 를 생성한다.

```SQLITE
CREATE TABLE friends (
id INTEGER,
name TEXT,
location TEXT
);
```



##### 해당 테이블에 다음과 같이 데이터를 입력한다.

```sqlite
INSERT INTO friends
VALUE (1, 'Justin', 'Seoul'),
(2, 'Simon', 'New York'),
(3, 'Chang', 'Las Vegas'),
(4, 'John', 'Sydney');
```



##### 스키마를 다음과 같이 변경한다.

```sqlite
ALTER TABLE friends ADD COLUMN married INTEGER;

ALTER TABLE friends RENAME TO new_table_name;
```



##### 데이터를 다음과 같이 추가한다.

```sqlite
UPDATE friends SET location = 'LA', married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
```



##### married 가 0 인 데이터를 모두 삭제한다.

```sqlite
DELETE FROM friends WHERE married =0;
```



##### 테이블을 삭제한다.

```sqlite
DROP TABLE friends;
```

