import sys
sys.stdin = open('jungbank.txt')

def changenum(bn, tn):

    for i in range(len(bn)):
        if bn[i] == '1':
            bn[i] = '0'
            bch.append(int(''.join(bn),2))
            bn[i] = '1'
        else:
            bn[i] = '1'
            bch.append(int(''.join(bn), 2))
            bn[i] = '0'

    for i in range(len(tn)):
        if tn[i] == '1':
            tn[i] = '0'
            tch.append(int(''.join(tn),3))
            tn[i] = '2'
            tch.append(int(''.join(tn), 3))
            tn[i] = '1'
        elif tn[i] == '2':
            tn[i] = '0'
            tch.append(int(''.join(tn), 3))
            tn[i] = '1'
            tch.append(int(''.join(tn), 3))
            tn[i] = '2'
        else:
            tn[i] = '1'
            tch.append(int(''.join(tn), 3))
            tn[i] = '2'
            tch.append(int(''.join(tn), 3))
            tn[i] = '0'

T = int(input())
for tc in range(1, T+1):
    bnum, tnum = list(input()), list(input())
    bch = []
    tch = []
    changenum(bnum, tnum)

    result = 0
    for i in bch:
        if i in tch:
            result = i
            break
    print('#{} {}'.format(tc, result))



