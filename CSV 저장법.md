# CSV 저장법

```python
lunch = {
  '용성돌솥비빔밥':'054-474-7119',
  '별난짬뽕':'054-473-3040',
  '매콤돈가스':'054-472-2030'
}

# 1. string formatting
with open('lunch.csv','w') as f:
    for item in lunch.items():
        f.write(f'{item[0]},{item[1]}\r\n')

# 2. join
with open('lunch.csv','w') as f:
    for item in lunch.items():
        f.write(','.join(item)+'\r\n')

# 3. csv.writer
import csv
with open('lunch.csv','w') as f:
    csv_writer = csv.writer(f)
    for item in lunch.items():
        csv_writer.writerow(item)


# 4. csv.DictWriter
import csv
with open('names.csv', 'w', newline='') as f:
    fieldnames = ('first_name', 'last_name')
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```

### CSV READER

```python
# 1. split
with open('lunch.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(',')) # 개행 문자를 없애기 위해 strip() 필요

# 2. csv.reader
import csv
with open('lunch.csv', 'r') as f:
    items = csv.reader(f)
    for item in items:
        print(item)

# 3. csv.DictReader
import csv
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
```

### 주의사항

- 구글링 가능. 주변 학생들 상의 가능. 서로 설명 듣기 가능. but **코드 대신 작성 금지**. 반드시 직접 작성.
- 코드 가독성 (변수명 등 신중하게)
- 코드 가이드는 따로 없음. 함수를 만들던 class를 만들던 완전 자유 형식. 목표는 일단 원하는 데이터 csv로 잘 모으는 것(문제해결). 코드 파일도 같이 제출하긴 하지만, 코드를 깔끔하게 짜는 건 후순위.