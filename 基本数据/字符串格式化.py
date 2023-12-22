# 占位型字符串格式化
brand = "一点点"
product = "奶茶"
price = 16
print("%s品牌%s的价格是%s元钱" % (brand, product, price))

# 通过占位形式完成字符串和数字的拼接
print("%s品牌的%s的价格是%f元钱" % (brand, product, price))
"""
    字符串的占位符：%s
    整数型的占位符：%d
    浮点型的占位符：%f
"""

# 数字的精度限制    %m.n 其中m是宽度限制，n是小数点后位数限制（四舍五入）
num_int = 11
num_float = 3.1415
print("数字%s宽度限制为5的结果：%5d" % (num_int, num_int))
print("数字%s宽度限制为1的结果：%1d" % (num_int, num_int))
print("数字%s宽度限制为7，小数点保留2位的结果：%7.2f" % (num_float, num_float))
print("数字%s无宽度限制，小数点保留3位的结果：%.3f" % (num_float, num_float))

# 快速格式化   f“巴拉巴拉{变量}"
print(f"{brand}的{product}价格是{num_float}")

# 表达式的格式化————简化代码，不是所有计算都要用变量来进行存储的
product_m = "冰淇淋"
price_m = 12.5
num_m = 3
print("购买了%d个%s，总共消费%.2f元钱" % (num_m, product_m, num_m * price_m))
print(f"购买了{num_m}个{product_m}，总共消费{num_m * price_m}元钱")
