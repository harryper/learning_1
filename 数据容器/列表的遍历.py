def iterator_while(mylist):
    index = 0
    while index < len(mylist):
        print(mylist[index], end=' ')
        index += 1


Mylist = ['I', 'am', 'the', 'Queencard']
iterator_while(Mylist)
print()

def iterator_for(mylist):
    for x in mylist:
        print(x, end=' ')


# 小练习
My_list = range(1, 11, 1)
i = 0
while i < len(My_list):
    print(My_list[i], end=' ')
    i += 2
print("baga ")
for x in My_list:
    if x % 2 == 0:
        print(x, end=' ')
