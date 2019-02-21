import random
b = []
for i in range(50):
    a = random.randint(-10,10)
    b.append(a)
print("随机整数列表:",b)
c = []
d = []
for i in b:
    if( i > 0 ):
        c.append(i)
    elif (i < 0):
        d.append(i)
print("正数:",c)
print("负数:",d)