# 打印1到100的整数，除了能被3整除的数字，76以后的就不输出了
for i in range(1,101):
    if i > 76:
        break
    if i % 3 ==0:
        continue
    print(f"{i} ", end='')

# 嵌套循环语句中，中断关键词只能跳出当前循环
for i in range(3):
    print("语句1")
    for j in range(15):
        break
        print("语句2")
print("语句3")

# 综合案例——1万元给20名员工发奖金
import random
total = 10000
for i in range(1, 51):
    performance = random.randint(1,10)
    if total <= 0:
        print("奖金发完了，下个月再说吧")
        break
    if performance >= 5:
        print(f"第{i}号员工，绩效分为{performance}，发放奖金{(performance-4) * 200}元")
        total -= (performance-4) * 200
    else:
        print(f"第{i}号员工，绩效分为{performance}，没有奖金，下一位")
