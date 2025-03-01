#一行代码实现1到100的求和,range函数直接把1——100的数字包括
#一般sum的参数为元组或则列表
# print(sum([1,2,3,4,5]))
# print(sum(range(1,100)))

#内置函数中比较重要的：zip和sorted函数
#例题：将元组（“a”,"b"）和元组（1,2）组合成字典{“a”:1,"b":2},运用zip函数
# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))
# key = ("a","b")
# value = (1,2)
# print(dict(list(zip(key,value))))
# #一条语句将L = [(1,2),(3,4)]转换成[(1,3),(2,4)]
# L = [(1,2),(3,4)]
# print(list(zip(L[0],L[1])))

#sorted排序函数，类比于sort
l = [3,5,1,8,9,2]
print(sorted(l))
#考查自定义排序规则
# l = [("yuan",22),("rain",18),("today",99)]
# def room(item):
#     return item[0]
# print(sorted(l,key=room))
#
# dic = [{"name":"yuan","score":98},{"name":"summer","score":66},{"name":"Ye","score":88}]
# def sue(item):
#     return item["score"]
# print(sorted(dic,key = sue))
#sorted(数据名,键值,reverse = True)第三个默认为True，是翻转的意思,True从高到低
f_list = [{"name":"flower","score":[70,80,90]},{"name":"tree","score":[50,60,88]},{"name":"book","score":[66,77,89]}]
def soft(item):
    return item["score"][2]
print(sorted(f_list,key=soft))
print(sorted(f_list,key=soft,reverse=True))