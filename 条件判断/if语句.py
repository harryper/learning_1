# if语句要加冒号：，并且加4个空格
name = input("请输入你的名字")
if name == "喵崽":
    print("骑骑熊崽")
print(f"欢迎{name}光临")

# 小练习
print("欢迎来到喵崽乐园，猫猫免费，熊崽收费。")
age = input("请输入你的年龄：")
if int(age) > 18:
    print("您已成年，游玩需要补票100元。")
print("祝您游玩愉快。")
