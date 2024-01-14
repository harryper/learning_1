# for循环的临时变量作用域仅在循环内，如果想获取值，需要先定义全局变量
i = 0
for i in range(1,5):
    print(i)
print(i)