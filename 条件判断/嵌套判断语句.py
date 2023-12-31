# 如果变量后面程序不会再用到
"""
print("~~~欢迎来到王者峡谷！~~~")
if int(input("请输入你的年龄")) <= 18:
    print("您是未成年人，每天只能玩1小时王者荣耀")
elif int(input("请输入您的游戏等级（1~5）")) > 4:
    print("您是尊贵的王者会员，可以无限制畅玩")
elif bool(input("请问是否充值？（True/False）")):
    print("感谢您的充值，可以继续游戏~")
else:
    print("您今日的游戏时间已用，欢迎明天再来王者峡谷冒险")
"""
# 嵌套判断语句
print("~~~欢迎来到王者峡谷！~~~")
if int(input("请输入你的年龄：")) > 18:
    if int(input("请输入您的游戏等级（1~5）：")) < 4:
        print("低等级会员每天只能玩2小时，高等级会员每天可无限制畅玩")
        if input("请问您是否升级到高级会员？\n（Y/N）") == "Y":
            print("充值成功！恭喜您已经成为高级畅玩会员，请继续您的冒险吧~")
        elif input("请问是否充值？\n（True/False）").lower() == "true":
            print("感谢您的充值，可以继续游戏~")
        else:
            print("您今日的游戏时间已用，欢迎明天再来王者峡谷冒险")
else:
    print("您是未成年人，每天只能玩1小时王者荣耀")

"""
if (bool([])) :
    print("True")
else:
    print("False")
    
data = "True"
isTrue = data == str(True)
"""

# 小练习
print("公司发放礼物，")
age = int(input("您的年龄是："))
if age >= 18 and age < 30:
    if int(input("您入职时间多少年？")) > 2 or int(input("级别：\n")) > 3:
        print("领奖")
