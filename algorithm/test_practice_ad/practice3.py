import sys
sys.stdin = open('practice3.txt')


code = ['001101',
        '010011',
        '111011',
        '110001',
        '100011',
        '110111',
        '001011',
        '111101',
        '011001',
        '101111']

T = input()
L1 = []
for i in T:
    num = bin(int(i, 16))[2:]
    dif = 4- len(num)
    L1.append('0'*dif+num)
data = ''.join(L1)
result = []
while data and len(data)>=6:
    patt = data[:6]
    if patt in code:
        result.append(code.index(patt))
        data = data[6:]
    else:
        data = data[1:]

print(*result)