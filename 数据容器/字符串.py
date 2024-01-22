# 字符串也是一种数据容器，它的元素是一个个字符，并且不可修改
mystr = "I love you! XiongZai~ I'm your Queencard"
print(f"字符串mystr第5个元素是：{mystr[4]}")
print(f"字符串mystr倒数第1个元素是：{mystr[-1]}")

# 字符串的索引
value = mystr.index('you')
print(f"字符串mystr中'you'的起始下标是：{value}")

# replace替换方法，实际上是创建一个新的字符串
my_new_str = (mystr.replace("XiongZai", "MiaoZai").replace("Queencard", "XiangBao"))
print(my_new_str)

# split方法，按照某种字符把一个字符串切分成几段，并返回一个列表
mystr_list = mystr.split(' ')
print(mystr_list)

# strip方法，去除字符串前后空格
mystr2 = " I want to eat Pizza~ "
new_mystr2 = mystr2.strip()
print(new_mystr2)
mystr3 = "1221212211kjvsdnvjnvjiev1322"
new_mystr3 = mystr3.strip("12")
print(new_mystr3)

# count方法，统计某个字符串出现的次数
mystr4 = "i nsj os i snj i"
count = mystr4.count("i")
print(count)

# len方法，统计字符串的长度
length = len(mystr4)
print(length)