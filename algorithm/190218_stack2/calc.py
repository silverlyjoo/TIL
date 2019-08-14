text = '2+3*4/5'
nums = '0123456789'

result = []
sub_result = []

for i in text:
    if i in nums:
        result.append(i)
    else:
        sub_result.append(i)

for i in range(len(sub_result)):
    result.append(sub_result.pop())

print(''.join(result))