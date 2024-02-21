"""1、函数的多返回值"""
def test_return1():
    return 1
    return 2

def test_return2():
    return 1, 2, 'hello'

# 当函数有多个返回值时，可以用逗号分隔，接受返回值的时候也需要对应；
# 如果有多个return语句，只有第一个返回值有效，其他return语句都不在函数中执行

x = test_return1()
print(x)
x, y, z = test_return2()
print(x, y, z)

"""2、多种传参形式——位置参数、关键字参数、缺省参数、不定长参数"""
def user_info(name, age, gender):
    print(f"姓名是：{name},年龄是 {age}, 性别：{gender}")
# 位置参数
user_info('miaozai', 25, '女')

# 关键字参数
user_info(name='Queencard', gender='女', age=21)

# 缺省参数：给参数设定默认值，并且必须在参数排序的最后面
def user_sign(name, account, password='123456'):
    print(f"{name}你好，你的账号{account}的密码是：{password}")

user_sign('miaozai', 'yuzhuzheng98@gmail.com')
user_sign('miaozai', 'yuzhuzheng98@gmail.com', '000000')

# 不定长参数
def user(*args):
    print(f"args的类型是{type(args)}，内容是{args}")
user('cat', 'dog', 'pig', 1, True)
#用位置不定长参数时，把传参存储为一个元组tuple

def user_info2(**kwargs):
    print(f"kwargs的类型是{type(kwargs)}，内容是{kwargs}")
user_info2(name='miaozai', age=17, ID='01')
# 用关键字不定长参数时，把传参存储为一个字典dict

