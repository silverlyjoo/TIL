-- 테이블 값 모두 가져오기
SELECT * FROM classmate;

-- 테이블의 특정 컬럼만 가져오기
SELECT id, name FROM classmate;

-- 특정 개수 가져오기 가져오는 ROW(레코드) 개수를 지정하기
SELECT id, name FROM classmate LIMIT 2

-- 가져오는 ROW(레코드)의 시작점 지정
SELECT * FROM classmate LIMIT 1 OFFSET 2;

-- 특정한 값을 가진 row 데이터 가져오기
SELECT * FROM classmate WHERE address='서울';