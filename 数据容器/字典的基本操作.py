# 字典中更新or新增元素
my_dict1 = {'喵崽': 99, '熊崽':97, '兔崽':70}
my_dict1['虎崽'] = 80
my_dict1['兔崽'] = 90
print(my_dict1)

# 删除元素
score = my_dict1.pop('虎崽')
print(f"字典移除一个元素后变为{my_dict1}，虎崽的分数是{score}")

# 清空元素
my_dict1.clear()
print(my_dict1)

# 获取全部的key
my_dict1 = {'喵崽': 99, '熊崽':97, '兔崽':90}
keys = my_dict1.keys()
print(f"所有的键值是：{keys}")
# 输出为：dict_keys(['喵崽', '熊崽', '兔崽'])

# 遍历字典
for x in keys:
    print(f"{x}的成绩是：{my_dict1[x]}")
"""  x取键值keys或字典都可以
for x in my_dict1:
    print(f"{x}的成绩是：{my_dict1[x]}")
"""

# 统计字典中的元素数量
count = len(my_dict1)
print(f"字典中元素的数量是：{count}")

# 小练习
employee = {'王力宏':{
        '部门': '科技部',
        '工资': 3000,
        '级别': 1
    }, '周杰伦':{
        '部门': '市场部',
         '工资': 5000,
        '级别': 2
    }, '林俊杰':{
        '部门': '研发部',
        '工资': 7000,
        '级别': 3
    }, '刘德华':{
        '部门': '文艺部',
        '工资': 6000,
        '级别': 2
    }
}
# for循环，对所有级别为1级的员工，薪水增加1000元，并且职位上升一级；
for x in employee:
    if employee[x]['级别'] == 1:
        employee[x]['级别'] += 1
        employee[x]['工资'] += 1000
print(employee)
