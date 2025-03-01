from time import perf_counter

s = "hello world"
#索引 ：字符串[索引]查询字符
print(s[6])
print(s[0])
print(s[-7])
#切片操作 字符串[开始索引：结束索引]顾头不顾尾
print(s[0:5])
print(s[6:11])
print(s[6:])#不写后项，表示缺省，直接取到最后一个值
print(s[ :5])
print(s[3:-2])
#只能从左向右切，不能从右到左
#新颖方法，隔一个取一个：：：
print(s[0:5:2])
#翻转
print("s[ ：]",s[ : ])
print("s[::-1]",s[ : :-1])

#拼接操作
s1 = "ty"
s2 = "gyh"
print(s1+s2)
print("1"*10)
#计算字符串的长度 内置函数len
s4 = "wooting"
print(len(s4))

#判断某个成员是否在字符串中，针对容器类型，in判断
s6 = "everyone have a dream"
print("everyone" in s6)
print("dreme" in s6)