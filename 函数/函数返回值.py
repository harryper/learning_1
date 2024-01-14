# 用return表示返回值，并且return之后的语句都不执行了
def buy(account, price, quan):
    consumption = price * quan
    print(f"您消费的金额是{consumption:.2f}, 账户余额{account - consumption:.2f}元")
    return account - consumption

buy(1000, 5,3)

# 如果函数没有定义return值，那自动返回None，类型是NoneType
def check_age(age):
    if age >= 18:
        return "Success"
    else:
        return None

result = check_age(17)
print(f"{result}的类型是{type(result)}")

if not check_age(17):
    print("未成年，可以上网吧玩~")

# None用于定义无初始内容的变量
name = None