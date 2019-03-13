# 190130 WORKSHOP

### sqlite basic



##### 아래 표와 같은 스키마를 가진 DB 테이블을 생성하고, 아래와 같이 Data 를 입력해 봅시다.

```sqlite
CREATE TABLE bands (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
debut INTEGER
);

INSERT INTO bands (name, debut)
VALUES ('Queen', 1973),
('Coldplay', 1998),
('MCR', 2001);
```



##### bands 테이블에서 모든 데이터 레코드의 id 와 name 만 조회하는 Query 를 작성하라.

```sqlite
SELECT id, name FROM bands;
```



##### bands 테이블에서 debut 가 2000 보다 작은 밴드들의 이름만을 조회하는 Query 를 작성하라.

```sqlite
SELECT name FROM bands WHERE debut < 2000;
```

