#关键参数就是在调用函数传参时，直接对参数进行赋值

#例如    stu("龙正阳",age = 18,course = "python",country="HongKong")
#但是关键参数不能放在位置参数之前，也就是 没有直接赋值的参数，：例如name
#参数优先级就是位置参数优于关键参数

# def stu(name,age,course,country = "China"):
#     print("姓名",name)
#     print("年龄",age)
#     print("国籍",country)
#     print("课程",course)
#
# stu("龙正阳",18,"python",country="HongKong")




#非固定参数，在已有参数的基础上加入其他需要加入的参数，并可以以元组或者字典的方式呈现
#def stu(name,age,*args):   元组：*args  字典：**kwargs
def stu(name,age,*args,**kwargs):
    print(name,age,args,kwargs)

stu("luffy",18,"python","java","c++",country="China",city="HongKong")




