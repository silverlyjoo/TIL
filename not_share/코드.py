d1 = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
d2 = {value:key + '*' * (len(value)-1) for key, value in d1.items() if len(value) <6 }
print(d2.keys())


# 1. a.extend('12')
# 2. a=list('12')
# 3. a.append('1').append('2')
# 4. a += ['1', '2']


# def func(*numbers):
# 	for number in numbers:
# 		if number % 5:
# 			print(number, end=', ')
# 		else:
# 			return number  
		
# print(func(1,3,5,7)) 


# for i in something:
#     if i == 't':
#         print(1)


# 1. something = {'a': 'apple', 'b': 'banana', 't': 'tomato'}
# 2. something = [('t')]
# 3. something = 'something'
# 4. something = [['t']]


# str = '4'
# print(str(3))


# def func(number):
#     sub = 1
#     while number > 0:
#         number -= sub
#         sub += 1
#         print(number, end='')

# func(5)


# s1 = "fun"
# s2 = "snake"
# s3 = "python"
# print(s3.replace(s2[s1.find("u")], "_"))


# 1. [x for x in range(5) if x % 2]
# 2. list(map(int, '1.3').split('.'))
# 3. list(range(5, 0, -2))[2:0:-1]
# 4. reversed(range(3, 0, -2))


# day_1 = [['Sunday', 'Monday'], 'Tuesday']
# day_2 = day_1
# day_3 = day_1[:]

# day_2[0][0] = 'Friday'
# day_3[0][1] = 'Thursday'

# sum = 0

# for i in (day_1, day_2, day_3):
#     if i[0][0] == 'Friday':
#         sum += 1
#     if i[0][1] == 'Thursday':
#         sum += 10

# print(sum)


# L = [1, 2, [3, 4], 5]
# print(L[3:0:-1])

# 1. [5, [3, 4]]
# 2. [5, [3, 4], 2]
# 3. [5, [4, 3], 2]
# 4. Syntax Error


# print("Welcome");print("to")
# print("Python");print("world!")

# 1. Welcometo
#    Pythonworld!

# 2. Welcome;to
#    Python;world!

# 3. Welcome
#    to
#    Python
#    world!

# 4. Welcome to
#    Python World!


# for i in range(1, 10):
#     if i % 2:
#         continue
#     print(i, end='')


# fruit = 100
# a = fruit is 100
# b = fruit == 100
# print(a, b)


# s = 'hello my name is ssafy'

# for i in s:
#     if i == 'm':
#         print(s)

# 1. m
#    m

# 2. hello my name is ssafy
#    hello my name is ssafy

# 3. m m

# 4. hello y nae is ssafy


# Python = "You need Python"
# print(Python.split())

# 1. ['You need Python']
# 2. You need Python
# 3. string은 split 함수가 없다
# 4. ['You', 'need', 'Python']


# L = ['1', '9', '10']
# print(L.sort())

# ssafy = {
#     'name': 'ssafy',
#     'learend': ['python3',
#                 'git',
#                 'Web'
#                 ],
#     'locations': {
#         '서울': '멀캠',
#         '대전': None,
#         '구미': '구미사업장',
#         '광주': '광주사업장'
#     }
# }


# import copy
# my_dict = {'zero': 0, 'odd': [1, 3, 5], 'even': [2, 4, 6]}

# dict1 = my_dict
# dict2 = dict(my_dict)
# dict3 = copy.copy(my_dict)
# dict4 = copy.deepcopy(my_dict)

# dict1['zero'] = 5
# dict2['odd'] = 7
# dict3['odd'] = [5]
# dict4['even'] = [8]



# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def greeting(self):
#         print(f'안녕하세요. {self.name}입니다.')

# hong = Person('홍길동')


# def func(c, b, a):
#     return a * b + c

# print(func(2, 5, 4))



