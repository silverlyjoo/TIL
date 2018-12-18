# 여러 줄 쓰기

# with open("multi_line.txt", "w", encoding = "utf-8") as f:
#     for i in range(1,11):
#         data = f'{i}번째 줄입니다.\n'
#         f.write(data)


# 리스트 쓰기

with open("count.txt", "w", encoding = "utf-8") as d:
    for i in range(1, 5):
        data = f'{i}번째 단어입니다.\t'
        d.writelines(data)

