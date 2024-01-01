# 喵崽喝奶茶循环
i = 1
while i < 7:
    i += 1
    print(f"第{i}天，喵崽不可以喝奶茶")
print(f"第{i}天，喵崽可以喝奶茶了")


# 小练习
import random
num = random.randint(1, 10)
print(num)
print("我心里想了一个从1到10的数字，请你猜猜是什么数字")

times = 1
while times < 4:
    i = int(input("请猜第%d次数字：\n" % times))
    if i == num:
        print("恭喜你猜对啦")
        times = 100
    elif i > num:
        print("猜大了")
    else:
        print("猜小了")
    times += 1

# 小练习
num = 1
Sum = 0
while num <= 100:
    Sum += num
    num += 1
print(Sum)

"""
while i != num and times < 4:
    i = int(input("请猜第%d次数字：\n" % times))
    if i > num:
        print("猜大了")
    else:
        print("猜小了")
    times += 1
if times <= 3:
    print("猜对啦")
    """
