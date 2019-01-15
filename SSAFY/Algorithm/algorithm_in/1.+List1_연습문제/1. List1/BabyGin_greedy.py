num = 112233 # baby-jin 확인할 6자리수
c = [0]*12   #6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
for i in range(6):
    c[num % 10] += 1
    num //= 10

i=0
tri = run = 0
while i < 10:
    if c[i] >= 3 : # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : #run 조사후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if tri + run == 2 : print("Baby Gin")
else : print("Lose")