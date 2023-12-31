# if和else语句要在同一个水平线上

print("欢迎来到喵崽乐园，猫猫免费，熊崽收费。")
age = input("请输入你的年龄：")
if int(age) > 18:
    print("您已成年，游玩需要补票100元。")
else:
    print("您未成年，可以免费游玩")
print("祝您游玩愉快。")

# 小练习
hight = input("请输入你的身高（cm）：")
if int(hight) > 120:
    print("您的身高过120cm，游玩需要购票10元")
else:
    print(f"您的身高是{hight}cm，可以免费游玩")
print("祝您游玩愉快")