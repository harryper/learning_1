"""字典的元素是由键值对{Key:value}组成的
注意事项：
   1）字典不支持下标索引，只能用键值key查找响应的value；
   2）key和value可以是任意类型，但key不能是字典类型；
   3）字典内key不允许重复，如果重复添加键值后面的value会覆盖前面的
"""

# 定义字典
my_dict1 = {'喵崽': 99, '熊崽':97, '兔崽':50}
print(f"字典my_dict1是：{my_dict1}，类型是：{type(my_dict1)}")

# 定义空字典
dict_empty1 = {}
dict_empty2 = dict()
print(f"字典dict_empty1是：{dict_empty1}，类型是：{type(dict_empty1)}")

# 定义重复的键值（不可以，字典中key是唯一的）
# 如果重复定义了自动中的键值，后面的value会覆盖前面的
my_dict2 = {'喵崽': 87, '熊崽':97, '喵崽':99}
print(my_dict2)

# 在字典中基于key值获取value
score = my_dict1['喵崽']
print(f"字典中“喵崽”的分数是：{score}")

# 定义嵌套字典
stu_score_dict = {'王力宏':{
    '语文': 77,
    '数学': 66,
    '英语': 33
    }, '周杰伦':{
    '语文': 88,
    '数学': 86,
    '英语': 55
    }, '林俊杰':{
    '语文': 99,
    '数学': 96,
    '英语': 66
    }
}
print(stu_score_dict)

# 从嵌套字典中查信息
score22 = stu_score_dict['周杰伦']['数学']
print(f"周杰伦的数学成绩是{score22}")


