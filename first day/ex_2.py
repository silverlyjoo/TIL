numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = []
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(odd, "홀수입니다")
print(even, "짝수입니다")

