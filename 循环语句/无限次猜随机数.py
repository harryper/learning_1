import random
num = random.randint(1, 100)
print(f"生成的随机数是{num}")
times = 1
i = int(input(f"请输入你第{times}次猜的数字"))

while i != num:
    if i > num:
        print("猜大了")
    elif i < num:
        print("猜小了")
    times += 1
    i = int(input(f"请输入你第{times}次猜的数字"))

print(f"恭喜你，第{times}次猜对啦，正确数字是{num}")
