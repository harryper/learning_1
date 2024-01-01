# for循环是轮询方式，无法定义循环条件，只能对待处理数据集中依次处理
name = "IamQueencard"
for x in name:
    print(x)

# 小练习
name = "Miaozai is the only Queencard in the world!"
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"Miaozai is the only Queencard in the world!这句话中有{count}个字母a")