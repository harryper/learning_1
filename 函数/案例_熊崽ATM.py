# 实现ATM机的基本功能：查询余额check、存款deposit、取款withdraw、退出exit
password = 980101
balance = 10000

def login(name):
    global password
    psword = int(input(f"{name}您好，请输入您的密码：\n"))
    if name == "喵崽" and psword == password:
        return True
    else:
        return False

def ATM(name):
    if not login(name):
        print("密码错误，八嘎~")
        return
    print("-------------------主菜单--------------------")
    print(f"{name}您好，欢迎来到熊崽小荷包ATM。请选择操作：")
    print("查询余额  [输入1]")
    print("存款     [输入2]")
    print("取款     [输入3]")
    print("退出     [输入4]")
    choice = int(input("请输入您的选择："))
    if choice > 4 or choice < 1:
        choice = int(input("操作错误，请重新输入："))
    while choice != 4:
        if choice == 1:
            choice = check()
        elif choice == 2:
            choice = deposit()
        elif choice == 3:
            choice = withdraw()
    if choice == 4:
        print(f"{name}拜拜~欢迎下次再来")

def check ():
    """
    查询余额函数，显示账户的余额
    :param x: 传入账户余额
    :return: 传出用户下一步想执行的操作
    """
    global balance
    print(f"您的账户余额是{balance}元")
    y = int(input("接下来您想做的操作是："))
    if y > 4 or y < 1:
        y = int(input("操作错误，请重新输入："))
    return y

def deposit():
    """
    存款函数，用户输入存的钱，加到全局变量balance中存的账户余额中
    :param x: 用户输入要存入的钱数
    :return: 传出用户下一步想执行的操作
    """
    global balance
    x = int(input("请存入钱到ATM机：\n"))
    balance += x
    print(f"恭喜您，存款成功，账户余额{balance}元")

    y = int(input("接下来您想做的操作是："))
    if y > 4 or y < 1:
        y = int(input("操作错误，请重新输入："))
    return y

def withdraw():
    """
    取款函数，用户输入想取的金额，如果超过账户余额就提示要求重新输入
    :param x: 用户输入要取走的钱数
    :return: 传出用户下一步想执行的操作
    """
    global balance
    x = int(input("请输入要取的金额"))
    while x > balance:
        x = int(input("取出金额超过账户余额，请重新输入取款金额：\n"))
    balance -= x
    print(f"恭喜您，取款成功，账户余额{balance}元")

    y = int(input("接下来您想做的操作是："))
    if y > 4 or y < 1:
        y = int(input("操作错误，请重新输入："))
    return y

ATM("喵崽")
