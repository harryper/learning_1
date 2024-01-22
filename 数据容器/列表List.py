# Python中用数据容器来存储多个元素（数据）
# 有六中数据容器，分别是列表List、元祖tuple、字符串str、集合set、字典dict

# 列表的语法[元素1, 元素2, 元素3, ...]
name_list = ['MiaoZai', 'XiongZai', 'Queencard']
print(name_list)
print(type(name_list))

my_list = ['MiaoZai', 'is', 'Queencard', 666, True]
print(my_list)
print(type(my_list))

list_list = [[1, 2, 3], ['a', 'b', 'c'], True]
print(list_list)
print(type(list_list))

# 列表的下表索引来取出列表中的具体元素，从0开始，倒着从-1开始
print(my_list[1])
print(name_list[-1])
# 取出嵌套列表中的元素，不要超出列表索引范围
print(list_list[1][0])