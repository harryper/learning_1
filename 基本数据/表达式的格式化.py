# 表达式格式化
# 不需要定义每一个变量
print("1 + 1的结果是%d" % (1 + 1))
print(f"1 + 1的结果是 {1 + 1}")
print("字符串在python中的数据类型是%s" % type("zfc"))

# 股价计算小程序
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (
stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))


def summ(name, stock_price, stock_code, stock_price_daily_growth_factor, growth_days):
    print(f"公司XXX：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
    print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (
    stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))


summ(name, stock_price, stock_code, stock_price_daily_growth_factor, growth_days)


