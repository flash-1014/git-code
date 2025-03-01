#在函数里面修改全局变量
# x = 1
# def foo():
#     global x
#     x  =100
#
# foo()
# print(x)

#如何修改嵌套enclosing变量,在已有全局变量，以及嵌套循环中的第一套循环中的变量
x = 1
def doo():
    x =10
    def foo():
        #非局部nonlocal
        nonlocal x
        x =100
    foo()
    print(x)

doo()
#python的最大递归层数：1000
import sys
print(sys.getrecursionlimit())

#关于*args和**kwargs,*args代表接受任意数量的位置参数，**kwargs用于处理关键字参数，参数中国带有文字，关键字，用户信息等


