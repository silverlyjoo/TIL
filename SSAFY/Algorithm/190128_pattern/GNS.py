import sys

sys.stdin = open("GNS_input.txt", "r")

T = int(input())
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"


for t_case in range(T):
    N = input()
    ZRO = ''
    ONE = ''
    TWO = ''
    THR = ''
    FOR = ''
    FIV = ''
    SIX = ''
    SVN = ''
    EGT = ''
    NIN = ''
    data = list((map(str, input().split())))
    for i in data:
        if i == 'ZRO':
            ZRO += " ZRO"
        elif i == 'ONE':
            ONE += " ONE"
        elif i == 'TWO':
            TWO += " TWO"
        elif i == 'THR':
            THR += " THR"
        elif i == 'FOR':
            FOR += " FOR"
        elif i == 'FIV':
            FIV += " FIV"
        elif i == 'SIX':
            SIX += " SIX"
        elif i == 'SVN':
            SVN += " SVN"
        elif i == 'EGT':
            EGT += " EGT"
        elif i == 'NIN':
            NIN += " NIN"
    result = ZRO + ONE + TWO + THR + FOR + FIV + SIX + SVN + EGT + NIN
    print(f'#{t_case+1}\n{result.lstrip()}')