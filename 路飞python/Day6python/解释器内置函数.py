#function

#abs: 取绝对值
print(abs(-10))
a = [1,2,3,4,5,6,7]
#all:对列表或者字典里面所有值进行布尔值检测，只要有一个，返回false,全部合格，返回True
print((a))
#any :任意一个值为True即可
b = [1,2,9,0,3,5,4]
print((b))
#chr:ASCII码输出
print(chr(90))

#ord ：传ASCII码转化为对应的数或者符号
print(ord("A"))

#dict 生成一个空字典
print(dict())
#dir 解释器内置的一些默认参数
#
#list 空列表
#locals  打印当前程序（当前作用域）的所有变量名和变量值
name = "alex"
age = 22
print(locals())

#map
l = list(range(10))
print(l)
def calc(x):
    return x**2
#print(map(calc,l))并没有执行(迭代器)
for i in map(calc,l):
    print(i)

#max 在可运算的元组/列表里面找最大值
#min 找最小值
#sum 求和
print(max(l))
print(min(l))
print(sum(l))

#round 对小数进行四舍五入的函数
print(round(3.1415926,2))#3,14

#str 把一个数据转化为字符串类型：[1,2,3,4,5]
print(str(123))

#zip
#fliter