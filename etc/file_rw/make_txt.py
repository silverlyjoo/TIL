#making text file

# f = open("new.txt", "w")
# f.write("Hello world!")
# f.close()

# with open("new.txt", "w") as f:
#     f.write("Hello !!")

# with open("new.txt", "a") as f:
#     f.write("World")

# f = open("new.txt", "r")
# data = f.read()
# print(data)
# f.close()

# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)


# f = open("new.txt", "w")
# for i in range(1, 5):
#     data = f'{i}번째 줄입니다. \n'
#     f.write(data)
# f.close()


# with open("new.txt", "w", encoding='utf-8') as f:
#     for i in range(1, 11):
#         data = f'{i}번째 줄입니다. \n'
#         f.write(data)

menu = ["밥\n", "김치\n", "삼겹살\n", "파채\n", "쌈장\n", "상추\n"]

# with open("menu.txt", "w", encoding = "utf-8") as f:
#     f.writelines(menu)
#     f.close

f = open("menu.txt", "w", encoding = "utf-8")
f.writelines(menu)
f.close()
