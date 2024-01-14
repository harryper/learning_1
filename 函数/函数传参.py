# 给定义函数传入参数
# x和y成为形式参数（形参）
def jiafa(x, y):
    y = y + x
    return y

x = 1
y = 2
# 1和2是实际参数（实参）
result = jiafa(x, y)
print(result)
print(y)

# 小练习
def hesuan():
    print('欢迎来到熊崽派对，请出示您的健康码以及72小时核酸证明，并配合体温测量！')
    cent = float(input('体温测量中：'))
    if cent <= 36.5:
        print(f"您的体温是：{cent}度，体温正常请进！")
    else:
        print(f"您的体温是：{cent}度，抓起来！")

hesuan()
