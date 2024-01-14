# 定义全局变量num
num = 100
def fun_a():
    print(f"fun_a：{num}")


def fun_b():
    num = 200    # 在函数内定义了一个局部变量，跟全局变量num没关系
    print(f"fun_b：{num}")

fun_a()
fun_b()
print(num)

def fun_c():
    global num
    num = 200    # 在函数内定义了一个局部变量，跟全局变量num没关系
    print(f"fun_c：{num}")

fun_c()
print(num)