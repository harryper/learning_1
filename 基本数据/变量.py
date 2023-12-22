# 定义一个变量，记录钱包余额
money = 9.15
# 打印余额
print("衬衫的价格是：", money, "便士")

# 买了一杯奶茶，花费5元钱
money -= 5
print("买了奶茶花费5元钱，还剩", money)

# 每隔一小时，输出一次钱包余额
print("现在是下午1点，钱包余额是：", money)
print("现在是下午2点，钱包余额是：", money - 1)
print("现在是下午3点，钱包余额是：", money - 2)
print("现在是下午4点，钱包余额是：", money - 3)

"""
变量课后练习

定义一个钱包，余额为 50 元，买奶茶用了10元，买烤串用了15元，打印余额
"""
money = 50
MilkTea = 10
Kaochuan = 15
money = money - MilkTea - Kaochuan
print("钱包剩余金额：", money)