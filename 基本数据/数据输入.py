# 输入你的名字
# print("你的名字是什么？")
# name = input()
# print("你是：%s" % name)

# print("你是：%s" % input())

# print("你是：%s" % input("你的名字是什么？"))

# 输入数值类型————input()只能识别string类型
password_i = input("请输入你的银行卡密码")
# print("你的银行卡密码类型是：%s" % type(name))
password = int(password_i)
print("你的银行卡密码类型是：", type(password))

# 小练习：
user_name = input("请输入您的用户名：\n")
user_type = input("请输入您的用户类型：\n")
print(f"您好：{user_name}，您是尊贵的：{user_type}用户，欢迎您光临。")



