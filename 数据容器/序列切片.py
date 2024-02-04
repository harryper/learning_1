# 序列切片[X, Y, Z]就是把列表、元组、字符串从起始第X到第Y个元素（不包含Y），
# 按照步长Z取出来（间隔Z-1），生成一个新的序列

# 对List进行切片，从1开始到4结束，步长为1
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = my_list[0:4]
print(new_list)

#对tuple进行切片，从到到尾，步长1为
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
new_tuple = my_tuple[:]
print(new_tuple)

# 对str进行切片，从头到尾，步长2
my_str = 'miao is queencard'
new_str = my_str[::2]
print(new_str)

# 对str进行切片，从头到尾，步长-1（倒着取元素）
my_str2 = '0123456789'
new_str2 = my_str2[::-1]
print(new_str2)

# 对列表进行切片，从3开始到1结束，步长-1
my_str3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_str3 = my_str3[2::-1]
print(new_str3)

# 对元祖进行切片，从头开始，到尾结束，步长-2
new_tuple2 = my_tuple[::-2]
print(new_tuple2)

# 小练习
my_str = "万过薪月，员序程马黑来，nohtyP学"
ym_str = my_str[::-1]
my_list = ym_str.split('，')
my_str2 = my_list[1][1:6]
print(my_str2)