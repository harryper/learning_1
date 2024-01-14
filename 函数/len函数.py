# 自己写一个函数，统计一个字符串有几位
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}个")

my_len("miaomiaomiao")

# 小练习
def hesuan(name):
    print(f"欢迎你 {name}用户！")
    print("请出示您的健康码以及72小时核酸证明")

hesuan("骑骑熊崽")