from itertools import filterfalse

age =21
if age>=18:
    print("成人小电影")
if age<18:
    print("青少年电影")

#直接使用bool值
b1 = False
b2 = True
print(b1)
print(b2)

#所有数据都有自己的bool值
print(2>1)
print(bool(1))
print(bool(0))#零值的bool状态为False，其他的值的bool状态都为True
print(bool(""))
print(bool(" "))#字符串的零值为空，只要有空格或者字或者数字其bool状态为True