#x,y都是形参只存在函数内部，在实参替换后直接释放
def calu(x,y):
    res = x*y
    print(res)

a = 5
b = 4
calu(a,b)#实参


#默认参数要放在最后
def stu(name,age,course,country = "China"):
    print("姓名",name)
    print("年龄",age)
    print("国籍",country)
    print("课程",course)

stu("龙正阳",18,"python",country="HongKong")