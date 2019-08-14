num = 131232
c = [0]*12
for i in range(6):
    c[num%10] += 1
    num //= 10
i = 0
tri = 0
run = 0

while i < 10 :
    print(c)
    if c[i] >=3:
        c[i] -= 3
        tri += 1
        print(c)
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        print(c)
        continue
    i += 1
if tri + run == 2: print('Baby_jin')
else: print('not')
print(c)

