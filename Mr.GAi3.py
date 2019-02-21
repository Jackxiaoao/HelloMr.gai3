import random
list = []
for i in range(20):
    num = random.choice(range(10))
    list.append(num)
print("列表长度:",len(list))
print("未排序:",list)
list[::2] = sorted(list[::2],reverse=True)
print("排序list:",list)