# elif语句，必须跟在if语句后面
print("~~~欢迎来到喵崽派对！~~~")
height = int(input("请输入你的身高（cm）："))
vip_level = int(input("请输入你的VIP级别（1~5级）"))
"""
if height > 120:
    if vip_level <= 3:
        print("您高于120CM，需要购票10元")
else:
    print(f"您的身高是{height}cm，可以免费游玩")
print("祝您游玩愉快")
"""
if height < 120:
    print(f"您的身高是{height}cm，可以免费游玩")
elif vip_level > 3:
    print(f"您是尊贵的{vip_level}级VIP用户，可以免费游玩")
else:
    print("不好意思，您是普通用户且高于120CM，需要购票10元")

# 如果变量后面程序不会再用到
print("~~~欢迎来到王者峡谷！~~~")
if int(input("请输入你的年龄")) <= 18:
    print("您是未成年人，每天只能玩1小时王者荣耀")
elif int(input("请输入您的游戏等级（1~5）")) > 4:
    print("您是尊贵的王者会员，可以无限制畅玩")
elif bool(input("请问是否充值？（True/False）")):
    print("感谢您的充值，可以继续游戏~")
else:
    print("您今日的游戏时间已用，欢迎明天再来王者峡谷冒险")

# 小练习
guess = 7
print("你来猜猜我想的是什么数字，在1到20之间哦")
if int(input("请输入你猜的第一个数字：")) == guess:
    print("恭喜你，猜对啦！")
elif int(input("不对，再猜一次：")) == guess:
    print("恭喜你，猜对啦！")
elif int(input("不对，再猜最后一次啦：")) == guess:
    print("恭喜你，猜对啦！")
else:
    print(f"Sorry都没猜对，我想的是{guess}")
