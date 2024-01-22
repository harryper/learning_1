# 方法——如果将函数定义为class的成员，那么这个函数就称为“方法”，例如：
"""
class Student:
    def add(self, x, y):
        return x + y

num = Student.add(1, 2)
"""
# 列表List的基本操作：增删改查
# 1）列表的增加、插入
mylist = ['I', 'am', 'Queencard']
mylist.insert(2, 'the')
print(f"插入元素之后的列表为：{mylist}")
mylist.append('!')
print(f"在列表尾部追加一个元素后为：{mylist}")
mylist.extend(['You', 'wanne', 'be', 'my', 'Queencard'])
print(f"在列表尾部追加一批元素后为：{mylist}")

# 2）列表元素的删除
mylist = ['XiongZai', 'is', 'a', 'Queencard']
del mylist[3]
print(f"列表删除一个元素后为：{mylist}")
element = mylist.pop(-1)
print(f"删除列表中最后一个元素为：{element}")

mylist = [1, 22, 33, 1, 55, 1, 77]
mylist.remove(1)
print(f"移除元素'1'之后元素为：{mylist}")
# 清空列表
mylist.clear()
print(f"列表被清空后结果是：{mylist}")

# 3）列表元素的修改
mylist = ['banana', 'apple', 'orange', 'peach']
mylist[2] = 'cheery'
mylist[-3] = 'strawberry'
print(f"修改后的列表为：{mylist}")

# 4）列表元素的查找
mylist = ['cat', 'dog', 'pig', 'sheep']
index = mylist.index('cat')
print(f"cat元素在列表中的下标索引值是：{index}")
# index = mylist.index('queencard')            ——如果索引的元素不在列表内，就会报错is not in list
# print(f"cat元素在列表中的下标索引值是：{index}")
print(f"列表中第2个元素是”{mylist[1]}“")

# 5）统计列表中某元素的个数
mylist = [1, 22, 33, 1, 55, 1, 77]
num = mylist.count(1)
print(f"列表中元素‘1’的个数是：{num}")
length = len(mylist)
print(f"列表中元素的总数量是：{length}")


# 小练习
agelist = [21, 25, 21, 23, 22, 20]
agelist.append(31)
agelist.extend([29, 33, 30])
print(agelist)
print(agelist[0])
print(agelist[-1])
print(agelist.index(31))
