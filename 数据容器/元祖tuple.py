# 定义元祖
t1 = (1, 3, 5, 'hello', True)
t2 = ()
t3 = tuple()
print(f"t1的类型是{type(t1)}，内容是{t1}")
print(f"t2的类型是{type(t2)}，内容是{t2}")
print(f"t3的类型是{type(t3)}，内容是{t3}")

# 定义单个元素的元祖，要加逗号
t4 = ('Queencard')
print(f"t4的类型是{type(t4)}，内容是{t4}")

# 元组的嵌套
t5 = ((1, 3, 5), (2, 4, 6))
print(f"t5的类型是{type(t5)}，内容是{t5}")

# 下标索引读取元组中的元素
print(t5[1])
print(t5[0][1])

# 元组的查找
print(t5.index((1, 3, 5)))
print(f"元组t1中元素'hello'的下标是：{t1.index('hello')}")
# print(t5.index(5))

# 元组中元素个数的统计
t6 = (1, 22, 33, 1, 55, 1, 77)
print(f"元组t6中元素'1'的个数是：{t6.count(1)}")

# 统计元组的长度
print(f"元组t6中元素的个数有：{len(t6)}")

# 元组中的元素是不可修改删除的，但是如果元素是列表，其中的元素可以修改
t7 = (1, 2, 'cat', [3, 7])
print(t7)
t7[3][1] = 4
print(t7)

# 小练习

t8 = ('周杰伦', 11, ['football', 'music'])

index = t8.index(11)
print(index)

name = t8[0]
print(name)

del t8[2][0]
print(t8)
fav = t8[2]
del(fav[0])
print(f'爱好是：{fav}')


fav.append('coding')

print(t8)