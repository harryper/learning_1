#  不换行符：, end = ' '
#  制表符：\t

# 打印九九乘法表
# 大循环：用i控制行数1~9
i = 0
while i < 9:
    i += 1
    j = 1
# 小循环：用j控制列数1~i
    while j <= i:
        print(f"{i}*{j}={i * j}\t", end='')
        j += 1
    print()