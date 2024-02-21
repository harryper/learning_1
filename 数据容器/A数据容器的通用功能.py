# 5类数据容器：列表list、元祖、tuple、字符串string、集合set、字典dictionary

# 定义数据容器变量
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = 'abcde'
my_set = {1, 2, 3, 4, 5}
my_dict = {'Key1':1, 'Key2':2, 'Key3':3, 'Key4':4, 'Key5':5}

# 统计元素个数
print(f"列表中元素的个数是：{len(my_list)}")
print(f"元组中元素的个数是：{len(my_tuple)}")
print(f"字符串中元素的个数是：{len(my_str)}")
print(f"集合中元素的个数是：{len(my_set)}")
print(f"字典中元素的个数是：{len(my_dict)}")

# Max找到最大元素、Min最小元素
print(f"列表中最大的元素是：{max(my_list)}")
print(f"元组中最大的元素是：{max(my_tuple)}")
print(f"字符串中最大的元素是：{max(my_str)}")
print(f"集合中最大的元素是：{max(my_set)}")
print(f"字典中最大的元素是：{max(my_dict)}")

# 类型转换， 把其他数据容器转换成List类型
dict = my_dict
print(f"字典转列表的结果是：{list(dict)}")

# 对元素进行排序（输出形式均为列表，my_dict会丢失value只保留键值）
print(f"对列表的元素进行排序：{sorted(my_list)}")
print(f"对元组的元素进行排序：{sorted(my_tuple)}")
print(f"对字符串的元素进行排序：{sorted(my_str)}")
print(f"对集合的元素进行排序：{sorted(my_set)}")
print(f"对字典的元素进行排序：{sorted(my_dict)}")

print(f"对列表的元素进行反向排序：{sorted(my_list, reverse = True)}")
"""
元素比较大小的底层逻辑---
每一个字符都对应一个ASCII码（数字），字符的比较本质上是ASCII码值的大小比较；
多个字符比较时，是从左到右一位一位的比较大小
"""
