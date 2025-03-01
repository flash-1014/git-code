#过滤函数filter
#lamdar,匿名函数，相当于构造函数，用的代码逻辑简单时使用
# l = [1,2,3,4,5,6]
# ret = filter(lambda item :item % 2 == 0,l )#filter(规则匿名函数，迭代数据)
# print(list(ret))
# #过滤列表中大于0的元素
# l2 = [-1,23,54,-4,6,-5,-43,32]
# ret =  filter(lambda it :it > 0,l2)
# print(list(ret))
#
# #复合数据
# b = [{"name":"wek","score":88},
#      {"name":"李四","score":99},
#      {"name":"张三","score":100},
#      {"name":"王五","score":66},
#      {"name":"赵六","score":77}]
# print(list (filter(lambda it:it["score"]>70,b)))
# #map
# #使用map函数将列表[1,2,3,4,5]转变[1,4,9,16,25]
# c = [1,2,3,4,5]
# print(list(map(lambda item:item*item ,c)))
# #map函数对列表a = [1,3,5],b = [2,4,6]相乘得到[2,12,30]
# a1 = [1,3,5]
# b1 = [2,4,6]
# print(list(map(lambda x,y:x*y,a1,b1)))

#将python is shell转成llehs si nohtyp每个单词做翻转
s = "python is shell"
l = s.split(" ")
print(l)
#!!!最后还要合并，字符串join函数
fina = " ".join(map(lambda item:item[::-1],l))
print(fina)
