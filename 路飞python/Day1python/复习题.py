# (1) 一行代码实现交换a和b两变量的值
# a = 4
# b = 5
# (a,b) =(b,a)
# print(a)
# print(b)
# (2) 用多个变量接受列表或元组的值
# l1 = [1,2,3,]
# a1,*a2 = l1
# print(a1,a2)
# t1 = (2,4,6,7,8)
# b1,b2,*b3 =t1
# print(b1,b2,b3)
# (3)输入一个字符串，返回倒序排列的结果。如abcdef,返回fedcba
# str1 = "abcdef"
# print(str1[::-1])
# (4)将“北京 上海 广州 深圳”变成“北京，上海，广州，深圳”
# str2 = "北京，上海，广州，深圳"
# ret = str2.split(" ")
# print(ret)
# str3 = "".join(ret)
# print(str3)
# (5)短路计算
# print(1 and 5)
# print(0 and 5)
# print(1 or 4)
# print(0 or 3)
# (6)o or 1 and 5
# print( 0 or 1 and 5)
# print(0 and 1 and 5)
# (6)将两个列表a =[1,5,7,9]和[2,2,6,8]合并[1,2,2,5,7,8,9]##合并加排序
# a1 = [1,5,7,9]
# b1 = [2,2,6,8]
#
# print(sorted(a1+b1))
# (7)a = [1,2,3,4,5,6],a[ ：：-3]结果
# a7 = [1,2,3,4,5,6]
# print(a7[::-3])
# (8)列表去重再排序
#集合直接去重，然后再转成列表
# lis = [1,2,2,4,5,6,7,7,9,10]
# ret = list(set(lis))
# print(ret)
# (9)s = 'ajdhjhdjadkdk'去重并从小到大排序
# s = 'ajdhjhdjadkdk'
# ret1 = sorted(set(s))
# print("".join(ret1))
# (10)python的三元运算表达
# x = 10
# # y =12
# # print(x if x>y else y )
# # a = 22
# # print("a是一个偶数" if a%2 ==0 else "a是一个奇数")
# (11)如何实现['1','2','3']变成[1,2,3]#字符转变为值
# a = ['1','2','3']
# print(list(int(i) for i in a))
# (12)获取1-100中所有偶数平方列表
# print(list(i*i for i in range(1,100)))
# (13)1,2,3,4,5能组成多少个互不相同且不重复的三位数
# l2 = [1,2,3,4,5]
# ret = []
# count = 0
# for i in l2:
#     for j in l2:
#         for k in l2:
#             if i != j and i != k and j != k:
#                 rew = str(i)+str(j)+str(k)
#                 ret.append(rew)
#                 count += 1
# print(ret)
# print(count)
# (14)交换字典中{'A':1,'b':2}
# d1 = {'A':1,'B':2}
# print({v:k for k,v in d1.items()})
# print({k:v+100 for k,v in d1.items()})
# (15)统计一段字符串中每个字符出现的次数，比如`abcaabccab`
# s = "abcaabccab"
# t1 = {}
# for c in s:
#     t1[c] = t1.get(c,0)+1
# print(t1)
# (16)在函数中修改全局变量
# x = 10
# def foss():
#     global x
#     x = 100
#修改嵌套enclosing变量，一般是嵌套循环
# x  = 10
# def boss():
#     x =100
#     def foss():
#         nonlocal x
#         x = 12
#     foss()
#     print(x)
# boss()
#实现一个翻转整数的函数-321翻转-123
# def reverse(value):
#     if value>-10 and value<10:
#         print(value)
#
#     if str(value)[0] !="-":
#         ret = int(str(value)[::-1])
#     else:
#         ret = -int(str(value)[1::][::-1])
#     print(ret)
# reverse(-123)