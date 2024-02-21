# 列表可以修改，支持重复元素且有序；元组和字符串不可修改，也支持重复元素
# 集合set不支持重复元素，且是无序的。set用{}来定义

# 定义集合（重复的元素自动合并）
my_set = {1, 2, 3, 1, 2, 3, 1, 2, 3}
myset_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set的内容是：{myset_empty}，类型是：{type(myset_empty)}")

# 添加新元素（集合是无序的，所以不支持下标索引）
my_set.add(4)
my_set.add(2)
print(f"my_set添加元素后变为：{my_set}")

# 移除元素
my_set.remove(3)
print(f"my_set移除元素“3”后变为：{my_set}")
# my_set.remove(5)              ---如果移除集合中本来不存在的元素，会报错
# print(f"my_set移除元素“5”后变为：{my_set}")

# 随机取出or丢弃一个元素
element = my_set.pop()
print(f"my_set随机弹出一个元素后变为：{my_set}，被弹出的元素是{element}")
my_set.discard(4)
print(f"my_set丢弃元素“4”后变为：{my_set}")

# 清空集合
my_set.clear()
print(f"my_set清空后是：{my_set}，类型是：{type(my_set)}")

# 取两个集合的差集
set1 = {1, 2, 3}
set2 = {1, 4, 5}
Difference_set1 = set1.difference(set2)
Difference_set2 = set2.difference(set1)
print(f"集合1有而集合2没有的差集是：{Difference_set1}")
print(f"集合2有而集合1没有的差集是：{Difference_set2}")
print(f"集合1{set1}、集合2{set2}本身没有变化")

# 消除两个集合的交集，集合本身被修改
set1.difference_update(set2)
set3 = {1, 4, 6}
set2.difference_update(set3)
print(f"集合1消除与集合2的交集后，变为：{set1}")
print(f"集合2消除与集合2的交集后，变为：{set2}")

# 两个集合取并集
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set_union1 = set1.union(set2)
set_union2 = set2.union(set1)
print(f"集合1、集合2的并集是：{set_union1}、{set_union2}")
print(f"集合1{set1}、集合2{set2}本身没有变化")

# 统计集合中元素数量
count = len(set1)
set3 = {1, 2, 3, 1, 2, 3}
count2 = len(set3)
print(f"集合1中元素的数量是：{count}；集合3中元素的数量是：{count2}")
# 集合没有count方法（统计某个元素的个数），因为集合中元素是没有重复的

# 集合的遍历
# 集合是无序的，不支持下标索引，因此不能用while循环来遍历；
my_set = {1, 2, 3, 4, 5, 6, 7}
for x in my_set:
    print(x, end=' ')

# 小练习（把列表中的元素放入到集合中）
my_list = ['cat', 'dog', 'rabbit', 'cat', 'dog', 'fox']
my_set = set()
for x in my_list:
    my_set.add(x)
print(my_set)
