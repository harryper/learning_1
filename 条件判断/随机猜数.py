import random
num = random.randint(1, 10)
print(num)
print("我心里想了一个从1到10的数字，请你猜猜是什么数字")
i = int(input("请猜第一次的数字：\n"))

temp = "猜对了"

if i == num:
    print(temp)
else:
    if i > num:
        temp = "猜大了"
    elif i < num:
        temp = "猜小了"

    i = int(input(temp + "，请猜第二次数字：\n"))
    if i == num:
        print(temp)
    else:
        if i > num:
            temp = "猜大了"
        elif i < num:
            temp = "猜小了"

        i = int(input(temp + "，请猜第三次数字：\n"))
        if i == num:
            temp = "猜对了！"
        else:
            if i > num:
                temp = "猜大了"
            elif i < num:
                temp = "猜小了"
        print(temp)