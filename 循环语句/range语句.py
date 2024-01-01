# range获得数字序列的语句
"""
range(num)生成数组[0,1,2,3...,num-1]
range(num1, num2)生成数组[num1, ..., num2-1]
range(num1, num2, step)，步进是step
"""

for x in range(10):
    print(f"{x} ",end='')
print()
for x in range(5, 10):
    print(f"{x} ", end='')
print()
for x in range(10, 11, 2):
    print(f"{x} ", end='')
print()

# 小练习
num = int(input("请随意输入一个正整数：\n"))
even = 0
for x in range(1, num+1):
    if x % 2 == 0:
        even += 1
print(f"从1到{num}范围内的偶数共有{even}个")
