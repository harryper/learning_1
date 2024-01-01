import random
num = random.randint(1, 10)
print(num)
print("我心里想了一个从1到10的数字，请你猜猜是什么数字")
num1 = int(input("请猜第一次的数字：\n"))
if num1 > num:
    print("猜大了")
    num1 = int(input("请猜第二个数字：\n"))
elif num1 < num:
    print("猜小了")
    num1 = int(input("请猜第二个数字：\n"))
    if num1 > num:
        print("猜大了")
        num1 = int(input("请猜第三个数字：\n"))
    elif num1 < num:
        print("猜小了")
        num1 = int(input("请猜第三个数字：\n"))
        if num1 > num:
            print("猜大了")
        elif num1 < num:
            print("猜小了")
        else:
            print("恭喜你猜对了")
    else:
        print("恭喜你猜对了")
else:
    print("恭喜你猜对了")



