# 王者荣耀做100天任务送新皮肤

for i in range(7):
    print(f"今天是您连续第{i+1}天做任务——已完成", end='')
    # 每天要完成5个任务
    for j in range(5):
        print(f"任务{j+1} ", end='')
    print()
print("恭喜您，完成任务获得新皮肤：喵之伸展！")

# for循环写九九乘法表
for i in range(1, 10):
    for j in range (1, i+1):
        print(f"{i}*{j}={i * j}\t", end='')
    print()
